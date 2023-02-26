# AI Video Convertor Based on ControlNet
## Inspiration 
If 2022 is a milestone of stable diffusion, when delicate AI generated drawings first better than human artists, then in 2023, the birth of ControlNet definitly push AI drawing generation to a new peak. It allows a stable, more controlled way of generate drawings. But is it just for drawing. In recently month, I have seen so much amazing AI Animation with stable diffusion. Those users just cut a video to different frames, render each frame, and put it together into delicate and consistent AI Animation. But can it be more convenient, user-friendly to handle this process? Here, our AI Video Convertor has born.
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
