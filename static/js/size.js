function tryer(FormData,con,blob) {
    console.log("wait");
    console.log(FormData);
    console.log(name);
    var resized=['image0','image1','image2']
    var name=['image0','image1','image2']
    console.log(resized[con]);
    FormData.append(resized[con],blob,name[con]);
    if(con==2)
    {
        var xhr = new XMLHttpRequest();

        xhr.open('POST', '/upload', true);
        xhr.send(FormData);
        location.reload();
    }
  }
function dataURItoBlob(dataURI) {
  
    var byteString = atob(dataURI.split(',')[1]);
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    } 
    return new Blob([ab], {type: mimeString});
}


function ResizeImage(callback) {
    var counter =0;
    var image =['imageFile0','imageFile1','imageFile2']
    var resized=['image0','image1','image2']
    var con=0;
    var name = [];
    var fd = new FormData(document.forms[0]);
for(var i=0;i<3;i++)
{
        var filesToUploads = document.getElementById(image[i]).files;
        var file = filesToUploads[0];
        //document.getElementById(image[i]).files ="";
        if (file) {
 
            var reader = new FileReader();
            // Set the image once loaded into file reader
            reader.onload = function(e) {
 
                var img = document.createElement("img");
                img.src = e.target.result;
               
                img.onload=function() {
                        console.log(con);
                        
                        var canvas = document.createElement("canvas");
                        var ctx = canvas.getContext("2d");
                        ctx.drawImage(img, 0, 0);

                        var MAX_WIDTH = 1000;
                        var MAX_HEIGHT = 1000;
                        var width = img.width;
                        var height = img.height;

                        if (width > height) {
                            if (width > MAX_WIDTH) {
                                height *= MAX_WIDTH / width;
                                width = MAX_WIDTH;
                            }
                        } else {
                            if (height > MAX_HEIGHT) {
                                width *= MAX_HEIGHT / height;
                                height = MAX_HEIGHT;
                            }
                        }
                        canvas.width = width;
                        canvas.height = height;
                        var ctx = canvas.getContext("2d");
                        ctx.drawImage(img, 0, 0, width, height);
                      //  console.log(img);
                        dataurl = canvas.toDataURL(file.type);
                      //  console.log(dataurl);
                        var blob = dataURItoBlob(dataurl);
                        
                      
                        for (var value of fd.values()) {
                            console.log(value); 
                         }  
                 
                        callback(fd,con,blob);
                        con++;
                    }
            }
            reader.readAsDataURL(file);
           
        }
    }   
 
}