# AI Video Convertor Based on ControlNet

## Inspiration:
In 2022, we witnessed a milestone in the world of AI-generated art, as delicate AI-generated drawings surpassed the skill of human artists. This achievement was followed in 2023 by the birth of ControlNet, which further pushed the boundaries of AI drawing generation by allowing for a stable and more controlled approach to creating drawings. In recent months, we have seen some incredible AI animations that are both delicate and consistent. These animations are created by cutting a video into individual frames, rendering each frame, and then putting them back together. But we wondered: could this process be made more user-friendly and convenient? "Our AI Video Converter is a powerful tool that transforms self-recorded or normal MMD videos into a variety of different styles, transfer between anime, realistic and more styles. With its potential to turn rough sketches into polished animations, it's a game-changer for the animation and film industries. With just a few clicks, you can enhance the quality of your videos and take your work to the next level."

## What we learned:
Throughout the development process, we learned a lot about how to interact with stable diffusion and ControlNet models using Python and JavaScript APIs. We also gained experience in running Python servers like Flask and interacting with Vue frontend. We learned how to process videos, including automatically separating them into frames and then converting them back into a video after AI generation.

## How we built our project:
We started by assigning tasks using Trello cards and creating a programming architecture flowchart to understand the structure of our entire program. We downloaded all the stable diffusion and ControlNet models onto one computer and tested them locally. We also created a local server to make it easier to switch to a crowd server. Finally, we used a web interface to make it easy for users to convert their videos in a user-friendly way.

## Challenges:
Developing this cutting-edge technology was a challenging experience for our team of four freshmen, particularly when it came to time management. Testing the API from ControlNet and debugging took a lot of time, with ten minutes required to test a single video. We had to work tirelessly without sleep for 24 hours to complete the project.


To run the server, follow the steps below:
1. Install flask and npm files
```
pip install flask
npm install
```
2. Go into the client folder and run dev
```
cd client
npm run dev
```
3. Ctrl-C to end hosting on 8080 (after building everything), go back to HackIllinois folder and build server
```
Ctrl-C
cd ../
python server.py
```
4. Go to "127.0.0.1:5000" and you will see everything
