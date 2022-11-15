import express from "express";
import { spawn } from "child_process";
import XLSX from "xlsx";
import formidable from "formidable";
const app = express();
const PORT = process.env.PORT || 3001;


app.post("/api/upload", function(req, res){
    const options = {
        keepExtensions: true
    }
    const form = new formidable.IncomingForm(options);
    form.parse(req, (err, fields, files) => {
    /* grab the first file */
        const f = Object.entries(files)[0][1];
        const path = f.filepath;
        const workbook = XLSX.readFile(path);

    /* DO SOMETHING WITH workbook HERE */
    res.send(path);
    // var process = spawn("py", ["./controllers/app.py", path]);
    // process.stdout.on("data", function(data){
    //     console.log(data.toString());
    // })
    // process.stderr.on('data', (data) => {
    //     console.error(data.toString());
    //   });
  });
})


app.listen(PORT, function(){
    console.log(`Server is running on port ${PORT}.`);
});