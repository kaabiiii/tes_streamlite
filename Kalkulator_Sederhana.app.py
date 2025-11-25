import streamlit as st

# Judul aplikasi
st.title("🅰️ Konverter Nilai ke Huruf")
st.write("Masukkan nilai Anda untuk mengetahui grade yang didapat")

# Input nilai dari user
nilai = st.number_input(
    "Masukkan nilai Anda:",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.1,
    help="Masukkan nilai antara 0 - 100"
)

# Tombol untuk memproses
if st.button("Cek Nilai"):
    # Cek nilai tidak valid (di luar rentang 0-100)
    if nilai > 100 or nilai < 0:
        st.error("❌ Nilai Anda tidak valid (di luar rentang 0-100)")
    # Cek Nilai A (85-100)
    elif nilai >= 85:
        st.success("🎉 **Nilai Anda A**")
        st.balloons()
    # Cek Nilai B (70-84.99...)
    elif nilai >= 70:
        st.success("👍 **Nilai Anda B**")
    # Cek Nilai C (55-69.99...)
    elif nilai >= 55:
        st.warning("✅ **Nilai Anda C**")
    # Cek Nilai D (40-54.99...)
    elif nilai >= 40:
        st.warning("⚠️ **Nilai Anda D**")
    # Sisanya adalah Nilai E (0-39.99...)
    else:
        st.error("💥 **Nilai Anda E**")

# Tambahkan informasi tentang kriteria penilaian
st.markdown("---")
st.subheader("📊 Kriteria Penilaian")
st.write("""
- **A**: 85 - 100
- **B**: 70 - 84.99
- **C**: 55 - 69.99
- **D**: 40 - 54.99
- **E**: 0 - 39.99
""")

# Versi alternatif dengan slider
st.markdown("---")
st.subheader("🎚️ Atau gunakan slider di bawah ini:")

nilai_slider = st.slider(
    "Pilih nilai dengan slider:",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.5
)

if st.button("Cek Nilai dari Slider"):
    if nilai_slider >= 85:
        st.success(f"🎉 **Nilai Anda A** (Nilai: {nilai_slider})")
        st.balloons()
    elif nilai_slider >= 70:
        st.success(f"👍 **Nilai Anda B** (Nilai: {nilai_slider})")
    elif nilai_slider >= 55:
        st.warning(f"✅ **Nilai Anda C** (Nilai: {nilai_slider})")
    elif nilai_slider >= 40:
        st.warning(f"⚠️ **Nilai Anda D** (Nilai: {nilai_slider})")
    else:
        st.error(f"💥 **Nilai Anda E** (Nilai: {nilai_slider})")
