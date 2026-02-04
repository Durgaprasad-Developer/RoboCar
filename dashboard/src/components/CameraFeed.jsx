export default function CameraFeed(){
    return (
        <div className="panel">
            <h2>Camera</h2>
            <img src="http://localhost:8000/video_feed" alt="camera feed" style={{width:"100%", borderRadius:"8px", border: "1px solid #334155" }}/>
        </div>
    )
}