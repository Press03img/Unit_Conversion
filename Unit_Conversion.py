import streamlit as st
from pint import UnitRegistry

# 単位換算用のライブラリ
ureg = UnitRegistry()

# サイドバーで換算対象を選択
category = st.sidebar.selectbox("換算する項目を選択", [
    "長さ", "面積", "体積", "質量", "力・重量", 
    "速度・速さ", "圧力・応力", "モーメント・トルク", "温度", "密度"
])

# 各カテゴリごとの単位リスト
unit_options = {
    "長さ": ["m", "cm", "mm", "km", "inch", "ft"],
    "面積": ["m²", "cm²", "mm²", "km²", "acre"],
    "体積": ["m³", "cm³", "L", "gal"],
    "質量": ["kg", "g", "lb", "ton"],
    "力・重量": ["N", "kN", "lbf"],
    "速度・速さ": ["m/s", "km/h", "mph"],
    "圧力・応力": ["Pa", "kPa", "MPa", "psi"],
    "モーメント・トルク": ["N·m", "kgf·m", "lbf·ft"],
    "温度": ["C", "F", "K"],
    "密度": ["kg/m³", "g/cm³", "lb/ft³"]
}

# ユーザー入力部分
st.write(f"**{category}の単位換算**")
from_unit = st.selectbox("変換元の単位", unit_options[category])
to_unit = st.selectbox("変換先の単位", unit_options[category])
value = st.number_input("変換する数値", value=0.0)

# 換算ボタン
if st.button("換算"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        result_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
        st.success(result_text)

        # クリップボードにコピーできるテキストボックス
        st.text_input("結果をコピー", result_text)

    except Exception as e:
        st.error(f"換算エラー: {e}")
