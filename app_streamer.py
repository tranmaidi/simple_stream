from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av

RTC_CONFIGURATION = RTCConfiguration(
    {
      "iceServers": [
      {
        "urls": ["stun:stun.relay.metered.ca:80"],
      },
      {
        "urls": ["turn:global.relay.metered.ca:80"],
        "username": "6d7b9ebe74cfcf3ff4d74844",
        "credential": "0yaGxZVrCZFteYcX",
      },
      {
        "urls": ["turn:global.relay.metered.ca:80?transport=tcp"],
        "username": "6d7b9ebe74cfcf3ff4d74844",
        "credential": "0yaGxZVrCZFteYcX",
      },
      {
        "urls": ["turn:global.relay.metered.ca:443"],
        "username": "6d7b9ebe74cfcf3ff4d74844",
        "credential": "0yaGxZVrCZFteYcX",
      },
      {
        "urls": ["turns:global.relay.metered.ca:443?transport=tcp"],
        "username": "6d7b9ebe74cfcf3ff4d74844",
        "credential": "0yaGxZVrCZFteYcX",
      },
      ]
    }
)

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx = webrtc_streamer(
    key="tmd",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)
