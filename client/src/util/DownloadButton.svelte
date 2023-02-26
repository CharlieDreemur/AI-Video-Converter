<script>
    export let url = null;

    import { download } from "./downloadVideo.js";

    function tryToDownload() {
        download(url)
            .then(() => errText = null)
            .catch(err => errText = err);
    }
    let errText = null;
</script>

<button on:click={tryToDownload}>Download</button>
{#if errText != null}
<p class="text-red-400">Error trying to download: {errText}</p>
{/if}