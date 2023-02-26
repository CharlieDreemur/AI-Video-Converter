# AI Video Convertor Based on ControlNet
## Inspiration 
If 2022 is a milestone of stable diffusion, when delicate AI generated drawings first better than human artists, then in 2023, the birth of ControlNet definitly push AI drawing generation to a new peak. It allows a stable, more controlled way of generate drawings. But is it just for drawing. In recently month, I have seen so much amazing AI Animation with stable diffusion. Those users just cut a video to different frames, render each frame, and put it together into delicate and consistent AI Animation. But can it be more convenient, user-friendly to handle this process? Here, our AI Video Convertor has born.

## What we learn
During this process, we learn so much about how to use python and javascript api to interact with stable diffusion and controlNet model. We also learn how to run python server such as flaxk and interact with Vue frontend. We learn how to process video such as autoally seperate video to frames and convert it back to video after AI generates. 

## How we built our project
We first use trello card to assign tasks and programming architecture flowchart to understand our whole program strucutre. We download all stable diffusion and controlNet model in one computer and test it locally. We also build a local server to support it easily to change to a crowd server. We use web to let users easily convert video in a user-friendly way.

## Challenge
Doing this new technology stuffs is such challengeable for our four freshmen, especially the time management. Using Api form ControlNet and test with local server spends us so much time, we have to spend 10 minutes to test one video and waste lots of time debugging. Our team members has to fight without sleep for 24 hours to finish this project.


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
