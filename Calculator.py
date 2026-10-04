import streamlit as st
import math

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Advanced Scientific Calculator")


# =========================================================
# SESSION STATE
# =========================================================

if "expression" not in st.session_state:
    st.session_state.expression = ""


# =========================================================
# CALCULATION FUNCTION
# =========================================================

def calculate_expression(expression):
    """Safely calculate a mathematical expression."""

    expression = expression.strip()

    # Automatically close missing brackets
    open_brackets = expression.count("(")
    close_brackets = expression.count(")")

    if open_brackets > close_brackets:
        expression += ")" * (open_brackets - close_brackets)

    # Math functions
    allowed = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "abs": abs,
        "pi": math.pi,
        "e": math.e,
    }

    result = eval(
        expression,
        {"__builtins__": {}},
        allowed
    )

    return result


# =========================================================
# BUTTON FUNCTIONS
# =========================================================

def add_value(value):
    st.session_state.expression += value


def clear_all():
    st.session_state.expression = ""


def delete_last():
    st.session_state.expression = (
        st.session_state.expression[:-1]
    )


# =========================================================
# INPUT MODE
# =========================================================

input_mode = st.radio(
    "Select Input Mode:",
    [
        "On-Screen Scientific Keyboard",
        "Direct Text Input"
    ],
    horizontal=True
)


# =========================================================
# DIRECT TEXT INPUT
# =========================================================

if input_mode == "Direct Text Input":

    st.subheader("⌨️ Direct Text Input")

    expression = st.text_input(
        "Enter Mathematical Expression",
        placeholder="Example: sin(30) + sqrt(16) * 5"
    )

    st.caption(
        "Examples: sin(30), cos(60), sqrt(25), log(100), 2**3"
    )

    if st.button(
        "🟢 Calculate Result",
        type="primary",
        use_container_width=True
    ):

        if expression.strip() == "":
            st.warning("Please enter an expression.")

        else:
            try:
                result = calculate_expression(expression)

                st.success(
                    f"Result: {result}"
                )

            except ZeroDivisionError:
                st.error(
                    "Cannot divide by zero."
                )

            except Exception:
                st.error(
                    "Invalid mathematical expression."
                )


# =========================================================
# ON-SCREEN CALCULATOR
# =========================================================

else:

    st.subheader("🖥️ Scientific Calculator")

    # -----------------------------------------------------
    # DISPLAY
    # -----------------------------------------------------

    st.text_input(
        "Display",
        value=st.session_state.expression,
        disabled=True
    )

    st.write("")

    # =====================================================
    # SCIENTIFIC FUNCTIONS
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "sin",
            on_click=add_value,
            args=("sin(",),
            use_container_width=True
        )

    with col2:
        st.button(
            "cos",
            on_click=add_value,
            args=("cos(",),
            use_container_width=True
        )

    with col3:
        st.button(
            "tan",
            on_click=add_value,
            args=("tan(",),
            use_container_width=True
        )

    with col4:
        st.button(
            "log",
            on_click=add_value,
            args=("log(",),
            use_container_width=True
        )

    with col5:
        st.button(
            "ln",
            on_click=add_value,
            args=("ln(",),
            use_container_width=True
        )


    # =====================================================
    # ADVANCED FUNCTIONS
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "√",
            on_click=add_value,
            args=("sqrt(",),
            use_container_width=True
        )

    with col2:
        st.button(
            "π",
            on_click=add_value,
            args=("pi",),
            use_container_width=True
        )

    with col3:
        st.button(
            "e",
            on_click=add_value,
            args=("e",),
            use_container_width=True
        )

    with col4:
        st.button(
            "^",
            on_click=add_value,
            args=("**",),
            use_container_width=True
        )

    with col5:
        st.button(
            "ABS",
            on_click=add_value,
            args=("abs(",),
            use_container_width=True
        )


    # =====================================================
    # 7 8 9 DELETE CLEAR
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "7",
            on_click=add_value,
            args=("7",),
            use_container_width=True
        )

    with col2:
        st.button(
            "8",
            on_click=add_value,
            args=("8",),
            use_container_width=True
        )

    with col3:
        st.button(
            "9",
            on_click=add_value,
            args=("9",),
            use_container_width=True
        )

    with col4:
        st.button(
            "DEL",
            on_click=delete_last,
            use_container_width=True
        )

    with col5:
        st.button(
            "CLEAR",
            on_click=clear_all,
            use_container_width=True
        )


    # =====================================================
    # 4 5 6 MULTIPLY DIVIDE
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "4",
            on_click=add_value,
            args=("4",),
            use_container_width=True
        )

    with col2:
        st.button(
            "5",
            on_click=add_value,
            args=("5",),
            use_container_width=True
        )

    with col3:
        st.button(
            "6",
            on_click=add_value,
            args=("6",),
            use_container_width=True
        )

    with col4:
        st.button(
            "×",
            on_click=add_value,
            args=("*",),
            use_container_width=True
        )

    with col5:
        st.button(
            "÷",
            on_click=add_value,
            args=("/",),
            use_container_width=True
        )


    # =====================================================
    # 1 2 3 PLUS MINUS
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "1",
            on_click=add_value,
            args=("1",),
            use_container_width=True
        )

    with col2:
        st.button(
            "2",
            on_click=add_value,
            args=("2",),
            use_container_width=True
        )

    with col3:
        st.button(
            "3",
            on_click=add_value,
            args=("3",),
            use_container_width=True
        )

    with col4:
        st.button(
            "+",
            on_click=add_value,
            args=("+",),
            use_container_width=True
        )

    with col5:
        st.button(
            "-",
            on_click=add_value,
            args=("-",),
            use_container_width=True
        )


    # =====================================================
    # 0 DECIMAL BRACKETS PERCENT
    # =====================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.button(
            "0",
            on_click=add_value,
            args=("0",),
            use_container_width=True
        )

    with col2:
        st.button(
            ".",
            on_click=add_value,
            args=(".",),
            use_container_width=True
        )

    with col3:
        st.button(
            "(",
            on_click=add_value,
            args=("(",),
            use_container_width=True
        )

    with col4:
        st.button(
            ")",
            on_click=add_value,
            args=(")",),
            use_container_width=True
        )

    with col5:
        st.button(
            "%",
            on_click=add_value,
            args=("/100",),
            use_container_width=True
        )


    # =====================================================
    # EQUAL BUTTON
    # =====================================================

    st.write("")

    if st.button(
        "🟢 =  CALCULATE",
        type="primary",
        use_container_width=True
    ):

        if st.session_state.expression.strip() == "":
            st.warning(
                "Please enter a calculation first."
            )

        else:

            try:

                result = calculate_expression(
                    st.session_state.expression
                )

                # Clean integer results
                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                st.session_state.expression = str(result)

                st.rerun()

            except ZeroDivisionError:

                st.error(
                    "Cannot divide by zero."
                )

            except ValueError:

                st.error(
                    "Invalid mathematical value."
                )

            except Exception:

                st.error(
                    "Invalid mathematical expression."
                )
