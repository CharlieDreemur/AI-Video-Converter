export async function submitFormInBackground(e) {
    return new Promise((resolve, reject) => {
    e.preventDefault();

    const ACTION_URL = e.target.action;

    const formData = new FormData(e.target);

    fetch(ACTION_URL, {
        method: e.target.method,
        body: e.target.method.toLowerCase() != "get" ? formData : undefined,
    })
        .then(res => resolve(res))
        .catch(rej => reject(rej));
    });
};

export function getFileExtension(filename) {
    return filename != null ? filename.substring(filename.lastIndexOf(".") + 1) : null;
}
