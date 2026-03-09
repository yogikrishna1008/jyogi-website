"""
Jyogi — Admin Panel
Only visible when logged in with ADMIN_PASSWORD.
Shows all readings, clients, orders, notes.
Full add / delete / download / upload Excel sync.
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from jyogi import logger as db


def _admin_stat(col, value, label, icon):
    with col:
        st.markdown(
            f'<div style="background:rgba(255,195,64,0.07);border:1px solid rgba(255,195,64,0.25);'
            f'border-radius:12px;padding:1rem;text-align:center;">'
            f'<div style="font-size:1.5rem;">{icon}</div>'
            f'<div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.6rem;margin:4px 0;">{value}</div>'
            f'<div style="color:rgba(232,224,208,0.5);font-size:0.72rem;text-transform:uppercase;'
            f'letter-spacing:1px;">{label}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )


def show_admin_panel():
    # ── Admin auth ───────────────────────────────────────────────────────────
    try:
        admin_pw = st.secrets.get("ADMIN_PASSWORD", "")
    except Exception:
        admin_pw = ""

    if not admin_pw:
        st.warning("⚠️ ADMIN_PASSWORD not set in secrets. Add it to enable admin access.")
        return

    if not st.session_state.get("admin_authenticated"):
        st.markdown("""
        <div style="max-width:380px;margin:3rem auto;text-align:center;">
            <div style="font-size:2rem;">🔐</div>
            <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.3rem;margin:8px 0;">
                Admin Access
            </div>
            <div style="color:rgba(232,224,208,0.5);font-size:0.82rem;font-style:italic;">
                This area is restricted to Jyogi only
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            pw = st.text_input("Admin Password", type="password",
                               placeholder="Enter admin password...",
                               label_visibility="collapsed")
            if st.button("🔓 Unlock Admin", use_container_width=True, type="primary"):
                if pw == admin_pw:
                    st.session_state["admin_authenticated"] = True
                    st.rerun()
                else:
                    st.error("❌ Wrong password.")
        return

    # ── Admin Header ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="display:flex;justify-content:space-between;align-items:center;
         padding:1rem 0 1.5rem;">
        <div>
            <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.5rem;">
                🔐 Admin Dashboard
            </div>
            <div style="color:rgba(232,224,208,0.45);font-size:0.8rem;">
                Jyogi internal — client records, readings, orders
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats bar ─────────────────────────────────────────────────────────────
    stats = db.get_stats()
    s1, s2, s3, s4, s5 = st.columns(5)
    _admin_stat(s1, stats["total_readings"],  "Total Readings",  "🔮")
    _admin_stat(s2, stats["astro_count"],     "Astrology",       "🪐")
    _admin_stat(s3, stats["tarot_count"],     "Tarot",           "🎴")
    _admin_stat(s4, stats["total_clients"],   "Clients",         "👤")
    _admin_stat(s5, stats["total_orders"],    "Orders",          "📦")

    st.markdown("<div style='margin:1.2rem 0;'></div>", unsafe_allow_html=True)

    # ── Excel sync bar ────────────────────────────────────────────────────────
    with st.expander("📥 Download / 📤 Upload Excel — Sync with your Mac", expanded=False):
        dl_col, up_col = st.columns(2)

        with dl_col:
            st.markdown("**📥 Download to Mac**")
            st.caption("Opens in Excel. Edit freely. Re-upload to sync.")
            try:
                excel_bytes = db.load_excel_bytes()
                st.download_button(
                    label="⬇️ Download jyogi_data.xlsx",
                    data=excel_bytes,
                    file_name=f"jyogi_data_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"Download error: {e}")

        with up_col:
            st.markdown("**📤 Upload from Mac**")
            st.caption("Upload your edited Excel to update the live data.")
            uploaded = st.file_uploader(
                "Upload Excel", type=["xlsx"],
                label_visibility="collapsed",
                key="admin_excel_upload",
            )
            if uploaded:
                if st.button("✅ Import & Replace Data", use_container_width=True):
                    ok, msg = db.import_excel(uploaded.read())
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

    st.divider()

    # ── Tabs ─────────────────────────────────────────────────────────────────
    t1, t2, t3, t4 = st.tabs([
        "🔮 Readings Log",
        "👤 Clients",
        "📦 Orders",
        "📝 Notes",
    ])

    # ════════════════════════════════════════════════════════════════════════
    # TAB 1 — READINGS LOG (auto-captured)
    # ════════════════════════════════════════════════════════════════════════
    with t1:
        st.markdown("##### All readings captured automatically from the website")
        df = db.get_sheet("Readings")

        if df.empty:
            st.info("No readings yet. They appear here automatically after users do a reading.")
        else:
            # Filter bar
            fc1, fc2, fc3 = st.columns(3)
            with fc1:
                type_filter = st.selectbox("Type", ["All", "Vedic Astrology", "Tarot"],
                                           key="r_type_filter")
            with fc2:
                search = st.text_input("Search client name", placeholder="Search...",
                                       key="r_search")
            with fc3:
                st.markdown(f'<div style="padding-top:30px;color:rgba(232,224,208,0.5);">'
                            f'{len(df)} total readings</div>', unsafe_allow_html=True)

            # Apply filters
            fdf = df.copy()
            if type_filter != "All":
                fdf = fdf[fdf["Type"] == type_filter]
            if search:
                fdf = fdf[fdf["Client Name"].str.contains(search, case=False, na=False)]

            # Show table newest first
            fdf_display = fdf.iloc[::-1].reset_index(drop=True)
            st.dataframe(
                fdf_display,
                use_container_width=True,
                height=400,
                column_config={
                    "Timestamp":      st.column_config.TextColumn("🕐 Time", width=130),
                    "Type":           st.column_config.TextColumn("Type", width=120),
                    "Client Name":    st.column_config.TextColumn("👤 Client", width=120),
                    "Birth Date":     st.column_config.TextColumn("DOB", width=90),
                    "Birth Time":     st.column_config.TextColumn("TOB", width=70),
                    "Birth Location": st.column_config.TextColumn("📍 Place", width=120),
                    "Spread":         st.column_config.TextColumn("Spread", width=140),
                    "Question":       st.column_config.TextColumn("❓ Question", width=250),
                    "Session ID":     None,  # hide
                },
            )

            # Delete a reading
            with st.expander("🗑️ Delete a reading row"):
                del_idx = st.number_input("Row number to delete (0 = top row)",
                                          min_value=0, max_value=max(len(fdf)-1, 0),
                                          value=0, key="r_del_idx")
                if st.button("Delete Row", key="r_del_btn", type="secondary"):
                    # Map filtered index back to original
                    real_idx = fdf_display.index[del_idx] if del_idx < len(fdf_display) else None
                    if real_idx is not None:
                        db.delete_row("Readings", int(real_idx))
                        st.success("Deleted.")
                        st.rerun()

    # ════════════════════════════════════════════════════════════════════════
    # TAB 2 — CLIENTS CRM
    # ════════════════════════════════════════════════════════════════════════
    with t2:
        df_c = db.get_sheet("Clients")

        # Add client form
        with st.expander("➕ Add New Client", expanded=len(df_c) == 0):
            with st.form("add_client_form", clear_on_submit=True):
                cc1, cc2 = st.columns(2)
                with cc1:
                    c_name  = st.text_input("Full Name *")
                    c_phone = st.text_input("Phone")
                    c_email = st.text_input("Email")
                    c_city  = st.text_input("City")
                with cc2:
                    c_dob   = st.text_input("Date of Birth", placeholder="e.g. 15-Mar-1990")
                    c_tob   = st.text_input("Time of Birth", placeholder="e.g. 14:30")
                    c_place = st.text_input("Birth Place")
                    c_notes = st.text_area("Notes", height=68)

                if st.form_submit_button("✅ Add Client", use_container_width=True):
                    if not c_name.strip():
                        st.warning("Name is required.")
                    else:
                        db.add_row("Clients", {
                            "Name":           c_name.strip(),
                            "Phone":          c_phone.strip(),
                            "Email":          c_email.strip(),
                            "City":           c_city.strip(),
                            "Date of Birth":  c_dob.strip(),
                            "Time of Birth":  c_tob.strip(),
                            "Birth Place":    c_place.strip(),
                            "Readings Done":  "0",
                            "Last Reading":   "",
                            "Notes":          c_notes.strip(),
                            "Added On":       datetime.now().strftime("%Y-%m-%d"),
                        })
                        st.success(f"✅ Client '{c_name}' added!")
                        st.rerun()

        if df_c.empty:
            st.info("No clients yet. Add your first client above.")
        else:
            search_c = st.text_input("🔍 Search clients", placeholder="Name, city, phone...",
                                     key="c_search")
            fdf_c = df_c.copy()
            if search_c:
                mask = df_c.apply(
                    lambda row: row.astype(str).str.contains(search_c, case=False).any(), axis=1
                )
                fdf_c = df_c[mask]

            st.dataframe(
                fdf_c.iloc[::-1].reset_index(drop=True),
                use_container_width=True,
                height=380,
                column_config={
                    "Name":          st.column_config.TextColumn("👤 Name", width=130),
                    "Phone":         st.column_config.TextColumn("📱 Phone", width=110),
                    "Email":         st.column_config.TextColumn("📧 Email", width=160),
                    "City":          st.column_config.TextColumn("📍 City", width=100),
                    "Date of Birth": st.column_config.TextColumn("DOB", width=100),
                    "Time of Birth": st.column_config.TextColumn("TOB", width=70),
                    "Birth Place":   st.column_config.TextColumn("Birth Place", width=120),
                    "Notes":         st.column_config.TextColumn("Notes", width=200),
                    "Added On":      st.column_config.TextColumn("Added", width=90),
                },
            )

            with st.expander("🗑️ Delete a client"):
                del_c = st.number_input("Row to delete", min_value=0,
                                        max_value=max(len(df_c)-1, 0), value=0, key="c_del")
                if st.button("Delete Client", key="c_del_btn", type="secondary"):
                    db.delete_row("Clients", int(del_c))
                    st.success("Deleted.")
                    st.rerun()

    # ════════════════════════════════════════════════════════════════════════
    # TAB 3 — ORDERS
    # ════════════════════════════════════════════════════════════════════════
    with t3:
        df_o = db.get_sheet("Orders")

        with st.expander("➕ Add New Order", expanded=len(df_o) == 0):
            with st.form("add_order_form", clear_on_submit=True):
                oc1, oc2 = st.columns(2)
                with oc1:
                    o_date   = st.text_input("Date", value=datetime.now().strftime("%Y-%m-%d"))
                    o_client = st.text_input("Client Name *")
                    o_phone  = st.text_input("Phone")
                    o_item   = st.selectbox("Item", [
                        "Money Magnet Bracelet", "Self-Love Mala",
                        "Protection Shield", "Third Eye Awakener",
                        "Lucky Charm", "Divine Feminine Bracelet", "Other",
                    ])
                with oc2:
                    o_amount   = st.text_input("Amount (₹)")
                    o_payment  = st.selectbox("Payment Status",
                                              ["Pending", "Paid", "Partial", "Refunded"])
                    o_delivery = st.selectbox("Delivery Status",
                                              ["Processing", "Shipped", "Delivered", "Cancelled"])
                    o_notes    = st.text_area("Notes", height=68)

                if st.form_submit_button("✅ Add Order", use_container_width=True):
                    if not o_client.strip():
                        st.warning("Client name required.")
                    else:
                        db.add_row("Orders", {
                            "Date":            o_date,
                            "Client Name":     o_client.strip(),
                            "Phone":           o_phone.strip(),
                            "Item":            o_item,
                            "Amount (₹)":      o_amount.strip(),
                            "Payment Status":  o_payment,
                            "Delivery Status": o_delivery,
                            "Notes":           o_notes.strip(),
                        })
                        st.success("✅ Order added!")
                        st.rerun()

        if df_o.empty:
            st.info("No orders yet.")
        else:
            # Revenue summary
            try:
                paid = df_o[df_o["Payment Status"] == "Paid"]["Amount (₹)"]
                total_rev = sum(int(str(x).replace("₹","").replace(",","").strip() or 0)
                                for x in paid if str(x).strip())
                st.markdown(
                    f'<div style="background:rgba(43,122,11,0.12);border:1px solid rgba(43,122,11,0.3);'
                    f'border-radius:10px;padding:10px 16px;margin-bottom:12px;display:inline-block;">'
                    f'💰 <strong>Total Revenue Collected:</strong> '
                    f'<span style="color:#90ee90;font-size:1.1rem;">₹{total_rev:,}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            except Exception:
                pass

            status_filter = st.selectbox("Filter by payment",
                                         ["All", "Paid", "Pending", "Partial", "Refunded"],
                                         key="o_status")
            fdf_o = df_o.copy()
            if status_filter != "All":
                fdf_o = df_o[df_o["Payment Status"] == status_filter]

            st.dataframe(
                fdf_o.iloc[::-1].reset_index(drop=True),
                use_container_width=True,
                height=360,
                column_config={
                    "Date":            st.column_config.TextColumn("📅 Date", width=90),
                    "Client Name":     st.column_config.TextColumn("👤 Client", width=130),
                    "Phone":           st.column_config.TextColumn("📱 Phone", width=110),
                    "Item":            st.column_config.TextColumn("💎 Item", width=180),
                    "Amount (₹)":      st.column_config.TextColumn("₹ Amount", width=90),
                    "Payment Status":  st.column_config.TextColumn("💳 Payment", width=100),
                    "Delivery Status": st.column_config.TextColumn("📦 Delivery", width=100),
                    "Notes":           st.column_config.TextColumn("Notes", width=180),
                },
            )

            with st.expander("🗑️ Delete an order"):
                del_o = st.number_input("Row to delete", min_value=0,
                                        max_value=max(len(df_o)-1, 0), value=0, key="o_del")
                if st.button("Delete Order", key="o_del_btn", type="secondary"):
                    db.delete_row("Orders", int(del_o))
                    st.success("Deleted.")
                    st.rerun()

    # ════════════════════════════════════════════════════════════════════════
    # TAB 4 — NOTES
    # ════════════════════════════════════════════════════════════════════════
    with t4:
        df_n = db.get_sheet("Notes")

        with st.form("add_note_form", clear_on_submit=True):
            nc1, nc2 = st.columns(2)
            with nc1:
                n_client  = st.text_input("Client Name")
                n_followup= st.text_input("Follow-up Date", placeholder="e.g. 2026-03-15")
            with nc2:
                n_note = st.text_area("Note / Observation", height=80)
            if st.form_submit_button("📝 Save Note", use_container_width=True):
                db.add_row("Notes", {
                    "Date":            datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Client Name":     n_client.strip(),
                    "Note":            n_note.strip(),
                    "Follow Up Date":  n_followup.strip(),
                    "Done":            "No",
                })
                st.success("Note saved.")
                st.rerun()

        if df_n.empty:
            st.info("No notes yet.")
        else:
            st.dataframe(
                df_n.iloc[::-1].reset_index(drop=True),
                use_container_width=True,
                height=360,
                column_config={
                    "Date":           st.column_config.TextColumn("🕐 Date", width=130),
                    "Client Name":    st.column_config.TextColumn("👤 Client", width=130),
                    "Note":           st.column_config.TextColumn("📝 Note", width=300),
                    "Follow Up Date": st.column_config.TextColumn("📅 Follow Up", width=110),
                    "Done":           st.column_config.TextColumn("✅ Done", width=70),
                },
            )

            with st.expander("🗑️ Delete a note"):
                del_n = st.number_input("Row to delete", min_value=0,
                                        max_value=max(len(df_n)-1, 0), value=0, key="n_del")
                if st.button("Delete Note", key="n_del_btn", type="secondary"):
                    db.delete_row("Notes", int(del_n))
                    st.success("Deleted.")
                    st.rerun()

    # ── Logout button ─────────────────────────────────────────────────────────
    st.divider()
    if st.button("🔒 Lock Admin Panel", type="secondary"):
        st.session_state["admin_authenticated"] = False
        st.rerun()
