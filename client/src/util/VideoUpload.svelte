<script>
	import { onMount } from 'svelte';
    import { stop_propagation } from 'svelte/internal';
    import { getFileExtension } from "./formSubmission";
    import VideoPlayer from "./VideoPlayer.svelte";

    export let file = null;

    const MAX_UPLOAD_SIZE_MB = 100;

    let fileInput = null;
    function promptUploadFile() {}
    onMount(() => {
        // redefine
        function promptUploadFile() {
            fileInput.click();
        }
    });

    function fileUpdated(e) {
		const potentialFile = e.target.files[0];
        const megaByteSize = potentialFile.size/Math.pow(10, 6);
        if (getFileExtension(potentialFile.name) !== "mp4") {
            errorText = `Files must be an mp4. (You uploaded a ${getFileExtension(potentialFile.name)})`;
            return;
        } else if (megaByteSize > MAX_UPLOAD_SIZE_MB) {
            errorText = `Max file size is ${MAX_UPLOAD_SIZE_MB} MB. (Your file is ${MAX_UPLOAD_SIZE_MB} MB.)`;
            return;
        }
		if (e == undefined) {
			file = null;
		} else {
			potentialFile.src = window.URL.createObjectURL(potentialFile);
		}
        file = potentialFile;
        errorText = null;
    }
    let errorText = null;
</script>

<div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500 cursor-pointer" on:click={promptUploadFile}>
    <label for="video" class="flex flex-col justify-center min-h-size-50">
        <p>Input</p>
        <div class="flex justify-center items-center text-center text-blue-500">
            {#if file == null}
                <span><!-- todo Drop Video Here <span class="block">- or -</span>--> Click to Upload</span>
            {:else}
            <VideoPlayer srcURL={file.src} type={getFileExtension(file.name)} trashVideo={() => file = null} />
            {/if}
            <input id="video" name="video" type="file" accept="video/mp4" class="hidden" bind:this={fileInput} on:change={fileUpdated} />
            {#if errorText != null}
            <p class="text-red-400">An error occurred: {errorText}</p>
            {/if}
        </div>
    </label>
</div>