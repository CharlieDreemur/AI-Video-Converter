export async function download(url) {
    return new Promise((resolve, reject) => {
        /*const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = 'blob';
        xhr.onload = function() {
            const imageUrl = window.URL.createObjectURL(this.response);
            const tag = document.createElement('a');
            tag.href = imageUrl;
            tag.target = '_blank';
            tag.download = 'sample.png';
            document.body.appendChild(tag);
            tag.click();
            document.body.removeChild(tag);
        };
        xhr.onerror = err => {
            reject(err);
        };
        xhr.send();*/

        fetch(url).then(res => res.blob()).then(file => {
            const tempUrl = URL.createObjectURL(file);
            const aTag = document.createElement("a");
            aTag.href = tempUrl;
            aTag.download = url.replace(/^.*[\\\/]/, '');
            document.body.appendChild(aTag);
            aTag.click();
            URL.revokeObjectURL(tempUrl);
            aTag.remove();
            resolve();
        }).catch(err => {
            reject(err);
        });
    });
}