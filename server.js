import express from "express";
import {resolve} from "path";
import { extname } from 'path';
import {promisify} from "util";
import {createReadStream, stat} from 'fs';
import axios from 'axios';

const app = express()
const PORT = 3001

app.use(express.static('Youtube/static'));

app.get('/', async (req, res) => {
    try {
        const djangoResponse = await axios.get('http://127.0.0.1:7000');
        res.send(djangoResponse.data);
    } catch (error) {
        console.error(`Error fetching Django page: ${error}`);
        res.status(500).send('Error fetching Django page');
    }
})


app.get('/api/stream', async (req, res) => {
    try {
        if(!req.query.video){
            console.log(`une erreur`)
        }
const validExtensions = ['mp4', 'mkv', 'mov', 'webm', 'flv', 'avi'];

if (!req.query.video.match(/^[a-z0-9-_ ]+\.(${validExtensions.join('|')})$/i)) {
  console.log(`une erreurtt`)
}

        const video = resolve('media', req.query.video)
        const videoInfos = await promisify(stat)(video)
        const rangeInfo = req.headers.range.replace('bytes=', "").split('-')
        const start = parseInt(rangeInfo[0], 10)
        const end = rangeInfo[1] ? parseInt(rangeInfo[1], 10) : videoInfos.size -1

        const header = {
            "Accept-range": 'bytes',
            "content-type": extname(video),
            "content-length": end - start +1,
            "content-range": `bytes ${start}-${end}/${videoInfos.size}`
        }

        res.writeHead(206, header)

        createReadStream(resolve('media/', req.query.video), {start, end}).pipe(res)



    } catch (error) {
        console.error(`Error fetching Django page: ${error}`);
        res.status(500).send('Error fetching Django page');
    }
});

app.listen(PORT, () =>{
     console.log(`le serverur ecoute sur le port ${PORT}`)
})