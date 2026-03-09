"""
Jyogi — Shop & Offerings Page
Luxury spiritual boutique UI.
"""
import json, os
import streamlit as st
from jyogi.inventory import BRACELETS, SERVICES, REVIEWS, GOD_GALLERY, WHATSAPP_NUMBER

# File to store user-submitted reviews
REVIEWS_FILE = "user_reviews.json"


def _wa_link(msg: str) -> str:
    import urllib.parse
    # Use wa.me format — works on mobile (opens app) and desktop (opens web)
    clean_number = WHATSAPP_NUMBER.strip().replace("+", "").replace(" ", "").replace("-", "")
    encoded_msg  = urllib.parse.quote(msg, safe="")
    return f"https://wa.me/{clean_number}?text={encoded_msg}"


def _load_user_reviews() -> list:
    """Load reviews submitted via the app form."""
    if os.path.exists(REVIEWS_FILE):
        try:
            with open(REVIEWS_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return []


def _save_review(review: dict) -> None:
    existing = _load_user_reviews()
    existing.insert(0, review)   # newest first
    with open(REVIEWS_FILE, "w") as f:
        json.dump(existing, f, indent=2)


def show_shop_page() -> None:

    # ── PAGE HEADER ───────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:2rem 1rem 1.5rem;">
        <div style="font-size:2.8rem;margin-bottom:0.4rem;">💎</div>
        <h1 style="font-family:Cinzel,serif;color:#FFC340;font-size:2.4rem;margin:0;letter-spacing:3px;">
            Sacred Offerings
        </h1>
        <p style="color:rgba(232,224,208,0.65);font-size:1rem;margin:0.5rem 0 0;letter-spacing:1px;">
            Hand-crafted crystal bracelets · Vedic consultations · Charged under moonlight
        </p>
        <div style="width:60px;height:2px;background:linear-gradient(90deg,transparent,#FFC340,transparent);
             margin:1rem auto 0;"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── TABS ─────────────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4 = st.tabs([
        "💎 Crystal Bracelets",
        "🔮 Book a Session",
        "⭐ Reviews",
        "🙏 Divine Gallery",
    ])

    # ════════════════════════════════════════════════════════════════════════
    # TAB 1 — CRYSTAL BRACELETS
    # ════════════════════════════════════════════════════════════════════════
    with tab1:
        st.markdown("""
        <p style="text-align:center;color:rgba(232,224,208,0.65);font-style:italic;
           max-width:600px;margin:0.5rem auto 1.5rem;">
            Every bracelet is hand-made in Rourkela, cleansed under the full moon,
            and charged with Vedic mantras before dispatch.
        </p>""", unsafe_allow_html=True)

        # Filter / sort bar
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            filter_chakra = st.selectbox(
                "Chakra", ["All Chakras", "Root", "Sacral & Crown", "Solar Plexus",
                           "Heart", "Third Eye & Crown"],
                label_visibility="collapsed",
            )
        with fc2:
            sort_by = st.selectbox(
                "Sort", ["Default", "Price: Low to High", "Price: High to Low"],
                label_visibility="collapsed",
            )
        with fc3:
            st.markdown(
                f'<div style="text-align:right;padding-top:8px;color:rgba(232,224,208,0.45);'
                f'font-size:0.82rem;">{len(BRACELETS)} items</div>',
                unsafe_allow_html=True,
            )

        items = list(BRACELETS)
        if filter_chakra != "All Chakras":
            items = [b for b in items if filter_chakra.lower() in b["chakra"].lower()]
        if sort_by == "Price: Low to High":
            items = sorted(items, key=lambda b: int(b["price"].replace("₹","").replace(",","")))
        elif sort_by == "Price: High to Low":
            items = sorted(items, key=lambda b: -int(b["price"].replace("₹","").replace(",","")))

        st.markdown("<div style='margin:0.5rem 0;'></div>", unsafe_allow_html=True)

        # Product grid
        for row_start in range(0, len(items), 2):
            row_items = items[row_start: row_start + 2]
            cols = st.columns(2)
            for col, b in zip(cols, row_items):
                with col:
                    _render_bracelet_card(b)

        # How to order guide
        st.divider()
        st.markdown("#### 📦 How to Order")
        hc1, hc2, hc3, hc4 = st.columns(4)
        for c, step, icon, txt in [
            (hc1, "1", "💬", "Click the WhatsApp button on any bracelet"),
            (hc2, "2", "📲", "Message is pre-filled — just tap Send"),
            (hc3, "3", "💳", "Jyogi shares UPI / bank details"),
            (hc4, "4", "📦", "Ships within 2–3 days, pan India"),
        ]:
            with c:
                st.markdown(
                    f'<div style="text-align:center;padding:14px 8px;background:rgba(255,195,64,0.04);'
                    f'border:1px solid rgba(255,195,64,0.12);border-radius:10px;">'
                    f'<div style="font-size:1.5rem;">{icon}</div>'
                    f'<div style="color:#FFC340;font-size:0.7rem;font-weight:700;margin:4px 0;">STEP {step}</div>'
                    f'<div style="color:rgba(232,224,208,0.55);font-size:0.75rem;line-height:1.4;">{txt}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

        # Nudge to leave a review
        st.markdown("<div style='margin:1rem 0;'></div>", unsafe_allow_html=True)
        st.markdown(
            '<div style="text-align:center;padding:1rem;background:rgba(255,195,64,0.04);'
            'border:1px solid rgba(255,195,64,0.12);border-radius:12px;">'
            '<span style="color:rgba(232,224,208,0.55);font-size:0.85rem;">Already received your bracelet? </span>'
            '<span style="color:#FFC340;font-size:0.85rem;">⭐ Head to the <strong>Reviews</strong> tab to share your experience!</span>'
            '</div>',
            unsafe_allow_html=True,
        )

    # ════════════════════════════════════════════════════════════════════════
    # TAB 2 — BOOK A SESSION
    # ════════════════════════════════════════════════════════════════════════
    with tab2:
        st.markdown("""
        <p style="text-align:center;color:rgba(232,224,208,0.65);font-style:italic;
           max-width:580px;margin:0.5rem auto 1.5rem;">
            Personal sessions with Jyogi via WhatsApp video call.
            All sessions include a follow-up message with key insights.
        </p>""", unsafe_allow_html=True)

        for i in range(0, len(SERVICES), 2):
            row_svcs = SERVICES[i: i + 2]
            cols = st.columns(len(row_svcs))
            for col, svc in zip(cols, row_svcs):
                with col:
                    _render_service_card(svc)

        # Trust badges
        st.markdown("<div style='margin:1rem 0;'></div>", unsafe_allow_html=True)
        tb1, tb2, tb3, tb4 = st.columns(4)
        for tc, icon, label in [
            (tb1, "🔒", "Secure Payment"),
            (tb2, "⚡", "Same Day Booking"),
            (tb3, "🌙", "Moon-Charged"),
            (tb4, "💯", "Satisfaction Guaranteed"),
        ]:
            with tc:
                st.markdown(
                    f'<div style="text-align:center;padding:12px 8px;background:rgba(255,195,64,0.05);'
                    f'border:1px solid rgba(255,195,64,0.15);border-radius:10px;">'
                    f'<div style="font-size:1.4rem;">{icon}</div>'
                    f'<div style="font-size:0.72rem;color:rgba(232,224,208,0.55);margin-top:4px;">{label}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<div style='margin:1rem 0;'></div>", unsafe_allow_html=True)
        st.markdown(
            '<div style="text-align:center;padding:1rem;background:rgba(255,195,64,0.04);'
            'border:1px solid rgba(255,195,64,0.12);border-radius:12px;">'
            '<span style="color:rgba(232,224,208,0.55);font-size:0.85rem;">Had a session with Jyogi? </span>'
            '<span style="color:#FFC340;font-size:0.85rem;">⭐ We would love to hear about it — visit the <strong>Reviews</strong> tab!</span>'
            '</div>',
            unsafe_allow_html=True,
        )

    # ════════════════════════════════════════════════════════════════════════
    # TAB 3 — REVIEWS
    # ════════════════════════════════════════════════════════════════════════
    with tab3:
        # Load all reviews (built-in + user-submitted)
        user_reviews = _load_user_reviews()
        all_reviews  = user_reviews + REVIEWS

        # Stats bar
        avg = sum(r["rating"] for r in all_reviews) / max(len(all_reviews), 1)
        s1, s2, s3 = st.columns(3)
        for sc, val, label in [
            (s1, f"{avg:.1f} / 5.0", "Average Rating"),
            (s2, f"{len(all_reviews)}+",  "Happy Clients"),
            (s3, "100%",              "Would Recommend"),
        ]:
            with sc:
                st.markdown(
                    f'<div style="text-align:center;padding:1rem;background:rgba(255,195,64,0.06);'
                    f'border:1px solid rgba(255,195,64,0.2);border-radius:12px;margin-bottom:1rem;">'
                    f'<div style="font-family:Cinzel,serif;font-size:1.9rem;color:#FFC340;">{val}</div>'
                    f'<div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;'
                    f'color:rgba(232,224,208,0.5);margin-top:4px;">{label}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<div style='margin:0.5rem 0;'></div>", unsafe_allow_html=True)

        # ── SUBMIT A REVIEW ─────────────────────────────────────────────────
        st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(255,195,64,0.08),rgba(43,122,11,0.06));
             border:1px solid rgba(255,195,64,0.3);border-radius:16px;padding:1.4rem 1.4rem 0.5rem;
             margin-bottom:1.2rem;">
            <div style="text-align:center;margin-bottom:1rem;">
                <div style="font-size:1.8rem;">✍️</div>
                <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.1rem;margin:4px 0;">
                    Share Your Experience
                </div>
                <div style="color:rgba(232,224,208,0.55);font-size:0.82rem;font-style:italic;">
                    Your story inspires others on their spiritual journey
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("review_form", clear_on_submit=True):
            rf1, rf2 = st.columns(2)
            with rf1:
                r_name = st.text_input("Your Name ✦", placeholder="e.g. Priya S.")
            with rf2:
                r_city = st.text_input("City", placeholder="e.g. Mumbai")

            r_product = st.selectbox(
                "What did you experience? ✦",
                ["Full Vedic Reading", "Live Tarot Session", "Crystal Prescription",
                 "Numerology Deep-Dive", "Money Magnet Bracelet", "Self-Love Mala",
                 "Protection Shield", "Third Eye Awakener", "Lucky Charm",
                 "Divine Feminine Bracelet", "Other"],
            )

            st.markdown(
                '<div style="color:rgba(232,224,208,0.7);font-size:0.82rem;margin:4px 0 2px;">Your Rating ✦</div>',
                unsafe_allow_html=True,
            )
            r_rating = st.select_slider(
                "Rating",
                options=[1, 2, 3, 4, 5],
                value=5,
                format_func=lambda x: "★" * x + "☆" * (5 - x),
                label_visibility="collapsed",
            )

            r_text = st.text_area(
                "Your Review ✦",
                placeholder="Share your experience — how did it help you? What changed in your life?",
                height=110,
            )

            st.markdown("<div style='margin:0.3rem 0;'></div>", unsafe_allow_html=True)
            r_submit = st.form_submit_button(
                "🙏 Submit My Review",
                use_container_width=True,
                type="primary",
            )

            if r_submit:
                if not r_name.strip() or not r_text.strip():
                    st.warning("⚠️ Please fill in your name and review.")
                elif len(r_text.strip()) < 20:
                    st.warning("⚠️ Please write at least 20 characters.")
                else:
                    new_review = {
                        "user":     r_name.strip(),
                        "location": r_city.strip() or "India",
                        "rating":   r_rating,
                        "product":  r_product,
                        "text":     r_text.strip(),
                        "avatar":   r_name.strip()[0].upper(),
                    }
                    _save_review(new_review)
                    st.success("🙏 Thank you! Your review has been added and is now visible below.")
                    st.balloons()
                    st.rerun()

        st.divider()
        st.markdown(
            '<div style="font-family:Cinzel,serif;color:#FFC340;font-size:1rem;'
            'text-align:center;margin-bottom:1rem;">⭐ What Others Are Saying</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='margin:0.4rem 0;'></div>", unsafe_allow_html=True)

        # Reviews grid
        for row_start in range(0, len(all_reviews), 3):
            row_revs = all_reviews[row_start: row_start + 3]
            cols = st.columns(3)
            for col, rev in zip(cols, row_revs):
                with col:
                    _render_review_card(rev)

    # ════════════════════════════════════════════════════════════════════════
    # TAB 4 — DIVINE GALLERY
    # ════════════════════════════════════════════════════════════════════════
    with tab4:
        st.markdown("""
        <p style="text-align:center;color:rgba(232,224,208,0.65);font-style:italic;margin-bottom:1.5rem;">
            May the divine light guide every step of your sacred journey. 🙏
        </p>""", unsafe_allow_html=True)

        g_cols = st.columns(len(GOD_GALLERY))
        for col, g in zip(g_cols, GOD_GALLERY):
            with col:
                st.image(g["img"], width="stretch")
                st.markdown(
                    f'<div style="text-align:center;padding:10px 0 16px;">'
                    f'<div style="font-family:Cinzel,serif;color:#FFC340;font-size:1rem;">{g["deity"]}</div>'
                    f'<div style="color:#ffe9a0;font-style:italic;font-size:0.85rem;margin:6px 0;">{g["mantra"]}</div>'
                    f'<div style="color:rgba(232,224,208,0.4);font-size:0.75rem;font-style:italic;">{g["meaning"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

        import random
        mantras = [
            ("Om Namah Shivaya",            "I bow to the inner self. I am divine consciousness."),
            ("Om Shreem Mahalakshmiyei Namah","I welcome abundance and grace into my life."),
            ("Om Gan Ganapataye Namah",      "All obstacles dissolve. New beginnings are blessed."),
            ("Om Dum Durgayei Namah",        "I am protected by divine power. I am fearless."),
            ("Om Shanti Shanti Shantihi",    "Peace flows through my body, mind, and spirit."),
        ]
        m_text, m_meaning = random.choice(mantras)
        st.markdown(
            f'<div style="background:linear-gradient(135deg,rgba(43,122,11,0.12),rgba(255,195,64,0.08));'
            f'border:1px solid rgba(255,195,64,0.25);border-radius:14px;padding:1.5rem;'
            f'text-align:center;margin-top:1.5rem;">'
            f'<div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:2px;'
            f'color:rgba(255,195,64,0.65);margin-bottom:10px;">✨ Today\'s Mantra</div>'
            f'<div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.3rem;">{m_text}</div>'
            f'<div style="color:rgba(232,224,208,0.55);font-style:italic;font-size:0.85rem;'
            f'margin-top:8px;">{m_meaning}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────────────────────────────────────
# COMPONENT: Bracelet card
# ─────────────────────────────────────────────────────────────────────────────
def _render_bracelet_card(b: dict) -> None:
    discount_pct = round(
        (1 - int(b["price"].replace("₹","").replace(",","")) /
             int(b["original_price"].replace("₹","").replace(",",""))) * 100
    )
    badge_html = (
        f'<span style="background:{b["badge_color"]};color:#fff;font-size:0.65rem;'
        f'font-weight:700;text-transform:uppercase;letter-spacing:1px;'
        f'padding:3px 9px;border-radius:12px;margin-left:6px;">{b["badge"]}</span>'
    ) if b.get("badge") else ""

    # Top colour bar based on stone colour
    st.markdown(
        f'<div style="height:3px;background:linear-gradient(90deg,{b["stone_color"]},{b["chakra_color"]});'
        f'border-radius:3px 3px 0 0;margin-bottom:-4px;"></div>',
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        # ── Product image ────────────────────────────────────────────────
        # Check if local image exists in products/ folder first
        local_img = None
        for ext in ("jpg", "jpeg", "png", "webp"):
            candidate = f"products/{b['id']}.{ext}"
            if os.path.exists(candidate):
                local_img = candidate
                break

        if local_img:
            st.image(local_img, width="stretch")
        else:
            st.image(b["img"], width="stretch")

        # ── Name + price ─────────────────────────────────────────────────
        st.markdown(
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;'
            f'margin:8px 0 4px;">'
            f'<div>'
            f'  <span style="font-family:Cinzel,serif;color:#fff;font-size:1rem;">{b["name"]}</span>'
            f'  {badge_html}'
            f'  <div style="color:rgba(232,224,208,0.5);font-size:0.75rem;margin-top:2px;">{b["subtitle"]}</div>'
            f'</div>'
            f'<div style="text-align:right;flex-shrink:0;margin-left:8px;">'
            f'  <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.15rem;">{b["price"]}</div>'
            f'  <div style="color:rgba(232,224,208,0.3);font-size:0.7rem;'
            f'       text-decoration:line-through;">{b["original_price"]}</div>'
            f'  <div style="color:#90ee90;font-size:0.68rem;">Save {discount_pct}%</div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div style="color:#ffe9a0;font-style:italic;font-size:0.8rem;margin:4px 0 8px;">'
            f'{b["tagline"]}</div>',
            unsafe_allow_html=True,
        )

        # Chakra + planet tags
        st.markdown(
            f'<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;">'
            f'<span style="background:rgba(255,195,64,0.09);border:1px solid rgba(255,195,64,0.2);'
            f'border-radius:20px;padding:2px 9px;font-size:0.68rem;color:#FFC340;">🪐 {b["planet"]}</span>'
            f'<span style="background:rgba(255,195,64,0.09);border:1px solid rgba(255,195,64,0.2);'
            f'border-radius:20px;padding:2px 9px;font-size:0.68rem;color:#FFC340;">✨ {b["chakra"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # Benefits + ritual in expander
        with st.expander("📖 Benefits & Ritual"):
            bc1, bc2 = st.columns(2)
            for idx, benefit in enumerate(b.get("benefits", [])):
                (bc1 if idx % 2 == 0 else bc2).markdown(
                    f'<span style="color:#90ee90;font-size:0.8rem;">✓ {benefit}</span>',
                    unsafe_allow_html=True,
                )
            st.markdown(
                f'<div style="background:rgba(255,195,64,0.06);border-left:3px solid rgba(255,195,64,0.4);'
                f'border-radius:0 8px 8px 0;padding:8px 12px;margin-top:10px;'
                f'font-size:0.78rem;color:rgba(232,224,208,0.7);">'
                f'🌙 <strong>Ritual:</strong> {b["ritual"]}</div>',
                unsafe_allow_html=True,
            )

        # WhatsApp order button
        wa_url = _wa_link(b["whatsapp_msg"])
        st.markdown(
            f'<a href="{wa_url}" target="_blank" style="display:block;text-decoration:none;margin-top:6px;">'
            f'<div style="background:linear-gradient(90deg,#25D366,#128C7E);color:#fff;'
            f'font-weight:700;text-align:center;padding:10px;border-radius:24px;'
            f'font-size:0.88rem;letter-spacing:0.5px;box-shadow:0 4px 14px rgba(37,211,102,0.28);">'
            f'📲 Order on WhatsApp — {b["price"]}'
            f'</div></a>',
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────────────────────────────────────
# COMPONENT: Service card
# ─────────────────────────────────────────────────────────────────────────────
def _render_service_card(svc: dict) -> None:
    wa_url = _wa_link(svc["whatsapp_msg"])
    includes_html = "".join(
        f'<div style="color:rgba(232,224,208,0.6);font-size:0.78rem;margin:3px 0;">'
        f'<span style="color:#2B7A0B;">✓</span> {inc}</div>'
        for inc in svc["includes"]
    )
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,195,64,0.2);'
        f'border-radius:16px;padding:20px;margin-bottom:1rem;">'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">'
        f'  <div>'
        f'    <span style="font-size:2rem;">{svc["icon"]}</span>'
        f'    <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1rem;margin-top:4px;">{svc["name"]}</div>'
        f'  </div>'
        f'  <div style="text-align:right;">'
        f'    <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.2rem;">{svc["price"]}</div>'
        f'    <div style="color:rgba(232,224,208,0.4);font-size:0.72rem;">⏱ {svc["duration"]}</div>'
        f'  </div>'
        f'</div>'
        f'<p style="color:rgba(232,224,208,0.65);font-size:0.83rem;margin:0 0 10px;line-height:1.6;">{svc["desc"]}</p>'
        f'{includes_html}'
        f'<a href="{wa_url}" target="_blank" style="text-decoration:none;display:block;margin-top:14px;">'
        f'<div style="background:linear-gradient(90deg,#25D366,#128C7E);color:#fff;'
        f'font-weight:700;text-align:center;padding:10px;border-radius:24px;font-size:0.88rem;">'
        f'📲 Book on WhatsApp</div></a>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
# COMPONENT: Review card
# ─────────────────────────────────────────────────────────────────────────────
def _render_review_card(rev: dict) -> None:
    stars = "★" * rev["rating"] + "☆" * (5 - rev["rating"])
    colors = {
        "A": "#c9910a", "R": "#2B7A0B", "P": "#9b2d8a",
        "D": "#1a6b8a", "M": "#8B0000", "S": "#4a4a6a",
        "K": "#5b3f8c", "N": "#2B7A0B", "V": "#8a6b1a",
    }
    av_color = colors.get(rev.get("avatar", "A"), "#555")
    avatar   = rev.get("avatar", rev["user"][0].upper())

    st.markdown(
        f'<div style="background:rgba(255,255,255,0.025);border:1px solid rgba(255,195,64,0.12);'
        f'border-radius:14px;padding:16px;margin-bottom:0.8rem;">'
        f'<div style="color:#FFC340;font-size:1rem;margin-bottom:8px;letter-spacing:2px;">{stars}</div>'
        f'<p style="color:rgba(232,224,208,0.75);font-style:italic;font-size:0.82rem;'
        f'line-height:1.6;margin:0 0 12px;">&ldquo;{rev["text"]}&rdquo;</p>'
        f'<div style="display:flex;align-items:center;gap:8px;border-top:1px solid rgba(255,195,64,0.1);'
        f'padding-top:10px;">'
        f'  <div style="width:32px;height:32px;border-radius:50%;background:{av_color};'
        f'       display:flex;align-items:center;justify-content:center;'
        f'       font-family:Cinzel,serif;font-size:0.85rem;color:#fff;flex-shrink:0;">{avatar}</div>'
        f'  <div>'
        f'    <div style="color:#e8e0d0;font-size:0.82rem;font-weight:600;">{rev["user"]}</div>'
        f'    <div style="color:rgba(232,224,208,0.4);font-size:0.7rem;">'
        f'        {rev.get("location","India")} · {rev.get("product","")}</div>'
        f'  </div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )
