import streamlit as st
import math

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Advanced Scientific Calculator")

# -----------------------------
# SAFE MATH FUNCTIONS
# -----------------------------
allowed = {
    name: value
    for name, value in math.__dict__.items()
    if not name.startswith("__")
}

# Extra useful functions/constants
allowed.update({
    "abs": abs,
    "round": round,
})

# -----------------------------
# INPUT MODE
# -----------------------------
input_method = st.radio(
    "Select Input Mode:",
    ["On-Screen Scientific Keyboard", "Direct Text Input"],
    horizontal=True
)

# ============================================================
# DIRECT TEXT INPUT
# ============================================================
if input_method == "Direct Text Input":

    st.subheader("⌨️ Keyboard Mode")
    st.caption(
        "Type any mathematical expression using your keyboard."
    )

    expr = st.text_input(
        "Enter expression:",
        placeholder="e.g. sin(pi/6) + sqrt(16) * 5"
    )

    if st.button(
        "Calculate Result",
        type="primary",
        use_container_width=True
    ):
        if not expr.strip():
            st.warning("Please enter a mathematical expression.")
        else:
            try:
                result = eval(
                    expr,
                    {"__builtins__": {}},
                    allowed
                )

                st.success(f"Result: {result}")

            except Exception:
                st.error(
                    "Invalid Math Syntax! Please check your expression."
                )


# ============================================================
# ON-SCREEN SCIENTIFIC KEYBOARD
# ============================================================
else:

    st.subheader("🖥️ Interactive Scientific Layout")

    # Initialize calculator input
    if "calc_input" not in st.session_state:
        st.session_state.calc_input = ""

    # -----------------------------
    # Helper Functions
    # -----------------------------
    def add_to_input(value):
        st.session_state.calc_input += str(value)

    def clear_input():
        st.session_state.calc_input = ""

    def backspace():
        st.session_state.calc_input = st.session_state.calc_input[:-1]

    # -----------------------------
    # Display
    # -----------------------------
    st.text_input(
        "Display Bar:",
        value=st.session_state.calc_input,
        disabled=True
    )

    # ========================================================
    # SCIENTIFIC FUNCTIONS
    # ========================================================
    st.markdown("### Scientific Functions")

    cols = st.columns(5)

    with cols[0]:
        st.button(
            "sin",
            on_click=add_to_input,
            args=("sin(",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            "cos",
            on_click=add_to_input,
            args=("cos(",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "tan",
            on_click=add_to_input,
            args=("tan(",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            "log",
            on_click=add_to_input,
            args=("log10(",),
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "ln",
            on_click=add_to_input,
            args=("log(",),
            use_container_width=True
        )

    # ========================================================
    # ADVANCED MATH
    # ========================================================
    cols = st.columns(5)

    with cols[0]:
        st.button(
            "√",
            on_click=add_to_input,
            args=("sqrt(",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            "π",
            on_click=add_to_input,
            args=("pi",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "e",
            on_click=add_to_input,
            args=("e",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            "^",
            on_click=add_to_input,
            args=("**",),
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "abs",
            on_click=add_to_input,
            args=("abs(",),
            use_container_width=True
        )

    # ========================================================
    # 7 8 9
    # ========================================================
    cols = st.columns(5)

    with cols[0]:
        st.button(
            "7",
            on_click=add_to_input,
            args=("7",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            "8",
            on_click=add_to_input,
            args=("8",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "9",
            on_click=add_to_input,
            args=("9",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            "DEL",
            on_click=backspace,
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "CLR",
            on_click=clear_input,
            use_container_width=True
        )

    # ========================================================
    # 4 5 6
    # ========================================================
    cols = st.columns(5)

    with cols[0]:
        st.button(
            "4",
            on_click=add_to_input,
            args=("4",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            "5",
            on_click=add_to_input,
            args=("5",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "6",
            on_click=add_to_input,
            args=("6",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            "×",
            on_click=add_to_input,
            args=("*",),
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "÷",
            on_click=add_to_input,
            args=("/",),
            use_container_width=True
        )

    # ========================================================
    # 1 2 3
    # ========================================================
    cols = st.columns(5)

    with cols[0]:
        st.button(
            "1",
            on_click=add_to_input,
            args=("1",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            "2",
            on_click=add_to_input,
            args=("2",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "3",
            on_click=add_to_input,
            args=("3",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            "+",
            on_click=add_to_input,
            args=("+",),
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "-",
            on_click=add_to_input,
            args=("-",),
            use_container_width=True
        )

    # ========================================================
    # 0 . ( ) %
    # ========================================================
    cols = st.columns(5)

    with cols[0]:
        st.button(
            "0",
            on_click=add_to_input,
            args=("0",),
            use_container_width=True
        )

    with cols[1]:
        st.button(
            ".",
            on_click=add_to_input,
            args=(".",),
            use_container_width=True
        )

    with cols[2]:
        st.button(
            "(",
            on_click=add_to_input,
            args=("(",),
            use_container_width=True
        )

    with cols[3]:
        st.button(
            ")",
            on_click=add_to_input,
            args=(")",),
            use_container_width=True
        )

    with cols[4]:
        st.button(
            "%",
            on_click=add_to_input,
            args=("/100",),
            use_container_width=True
        )

    # ========================================================
    # EQUAL
    # ========================================================
    if st.button(
        "=",
        type="primary",
        use_container_width=True
    ):

        expression = st.session_state.calc_input.strip()

        if not expression:
            st.warning("Please enter an expression.")
        else:
            try:
                result = eval(
                    expression,
                    {"__builtins__": {}},
                    allowed
                )

                st.session_state.calc_input = str(result)
                st.rerun()

            except ZeroDivisionError:
                st.error("Cannot divide by zero!")

            except Exception:
                st.error(
                    "Syntax Error! Please check your expression."
                )
