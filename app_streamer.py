from streamlit_webrtc import webrtc_streamer
import av

RTC_CONFIGURATION = RTCConfiguration(
    {
      "iceServers": [
      {
        urls: "stun:stun.relay.metered.ca:80",
      },
      {
        urls: "turn:global.relay.metered.ca:80",
        username: "62a780ff22906dc4804b8101",
        credential: "INzShUB/OF2KMxIJ",
      },
      {
        urls: "turn:global.relay.metered.ca:80?transport=tcp",
        username: "62a780ff22906dc4804b8101",
        credential: "INzShUB/OF2KMxIJ",
      },
      {
        urls: "turn:global.relay.metered.ca:443",
        username: "62a780ff22906dc4804b8101",
        credential: "INzShUB/OF2KMxIJ",
      },
      {
        urls: "turns:global.relay.metered.ca:443?transport=tcp",
        username: "62a780ff22906dc4804b8101",
        credential: "INzShUB/OF2KMxIJ",
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
