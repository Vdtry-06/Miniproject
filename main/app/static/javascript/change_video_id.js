// change_video_id.js

// Declare a global variable to store the videos data
let videos = [];

// Function to initialize the video player with video data passed from the Django view
function initializeVideos(videoData) {
    videos = videoData; // Store the video data passed from Django
    updateVideo(); // Initialize with the first video (or a default one)
}

// Function to get the index of a video by its ID
function getVideoIndexById(id) {
    return videos.findIndex(video => video.id === id);
}

// Function to update the video player with the current video
function updateVideo() {
    const videoIndex = getVideoIndexById(cur_id);
    if (videoIndex !== -1) {
        const video = videos[videoIndex];
        document.getElementById("videoSource").src = video.url;
        document.getElementById("videoTitle").textContent = video.title;
        document.getElementById("videoPlayer").load();
    }
}

// Function to go to the next video
function nextVideo() {
    const currentIndex = getVideoIndexById(cur_id);
    const nextIndex = (currentIndex + 1) % videos.length;  // Loop to the start
    cur_id = videos[nextIndex].id; // Update cur_id to next video ID
    updateVideo();
}

// Function to go to the previous video
function previousVideo() {
    const currentIndex = getVideoIndexById(cur_id);
    const prevIndex = (currentIndex - 1 + videos.length) % videos.length;  // Loop to the end
    cur_id = videos[prevIndex].id;  // Update cur_id to previous video ID
    updateVideo();
}
