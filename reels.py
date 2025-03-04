import streamlit as st
import yt_dlp
import time

# Streamlit UI Setup
st.set_page_config(page_title="Instagram Reel Downloader", page_icon="🎥", layout="centered")

st.title("📥 Instagram Reel Downloader")
st.markdown("🔹 Download Instagram reels easily by pasting the link below.")

# Input Box for Instagram Reel Link
link = st.text_input("📌 Enter Instagram Reel Link:", placeholder="Paste the Instagram reel URL here")

# Download Button
if st.button("🚀 Download Reel"):
    if link:
        try:
            st.info("🔄 Downloading... Please wait.")
            
            # YT-DLP Options for Download
            ydl_opts = {
                'outtmpl': f"reel_{int(time.time())}.mp4",  # Save file as reel_timestamp.mp4
                'format': 'bestvideo+bestaudio/best',  # Best available quality
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            st.success("✅ Reel downloaded successfully!")
            st.balloons()  # Celebration effect
            
        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
    else:
        st.warning("⚠ Please enter a valid Instagram reel link.")

# Footer
st.markdown("---")
st.caption("💡 Built with ❤️ using Streamlit & YT-DLP")
