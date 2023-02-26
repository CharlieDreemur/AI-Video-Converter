<script>
    let fps = 1;
    let videoData = null;
    $: serverVideoSrc = videoData == null ? null : `/dlv?dfn=${videoData.name}`; // bind

    import { getRandomAdjective } from "./randomAdjective.js";
    import { submitFormInBackground } from "./formSubmission.js";
    import DownloadButton from "./DownloadButton.svelte";
    import VideoPlayer from "./VideoPlayer.svelte";
    
	const uploadURL = "/upv";
	const samplingMethods = ["Euler a"]; // todo add
	const styles = ["anime", "realistic", "3D-anime", "art"];
	const types = ["general", "character", "building", "dance"];
    import { getFileExtension } from "./formSubmission";

    export let file = null;

    const MAX_UPLOAD_SIZE_MB = 100;

    let fileInput = null;
    function promptUploadFile() {
        fileInput.click();
	}
	/*
    onMount(() => {
        // redefine
		console.log("here mount")
        function promptUploadFile() {
			console.log("try click")
            fileInput.click();
        }
    });*/

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

    function submitVideoForm(e) {
		console.log(fileInput);
        submitting = true;
		console.log(e.srcElement);
        submitFormInBackground(e)
            .then(res => {
                submitting = false;
				if (res.status !== 200) {
					errorText = `Got a bad response from the server (${res.status})`;
				} else {
					// send up
					serverVideoReadyState = 2;
					console.log(serverVideoSrc);
					return res.text();
				}
            })
			.then(text => {
				// Handle text response if needed
			})
            .catch(err => {
                submitting = false;
                errorText = err.message;
            });
    }

    // let clientPrompt = null; //#prompt bind:value={clientPrompt}
	//$: promptHint = clientPrompt.length < 8 ? "Add more details" : null;

	const promptPlaceholder = `Make it ${getRandomAdjective()}`;
    let errorText = null;
    let submitting = false;
    
	let serverVideoReadyState = 0; // 0 = not started, 1 = processing, 2 = ready
</script>

<form action={uploadURL} method="POST" enctype="multipart/form-data" class="p-10 mx-auto bg-white rounded-xl shadow-lg space-y-4 grid" on:submit|preventDefault={submitVideoForm}>
	<input id="video" name="video" type="file" accept="video/mp4" class="hidden" bind:this={fileInput} on:change={fileUpdated}/>
	 <!-- disabled={file !== null} /> -->
	<div class="grid sm:grid-cols-2 justify-center text-center mt-8">
		<div>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500 cursor-pointer" on:click={promptUploadFile}>
				<label for="video" class="flex flex-col justify-center min-h-size-50">
					<p>Input</p>
					<div class="flex justify-center items-center text-center text-blue-500">
						{#if file == null}
							<span><!-- todo Drop Video Here <span class="block">- or -</span>--> Click to Upload</span>
						{:else}
						<VideoPlayer srcURL={file.src} type={getFileExtension(file.name)} trashVideo={() => file = null} />
						{/if}
					</div>
				</label>
			</div>
		</div>
        <div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500">
            <p>Output</p>
            {#if serverVideoReadyState === 2}
                <DownloadButton bind:url={serverVideoSrc} />
                <VideoPlayer bind:srcURL={serverVideoSrc} type={"mp4"} trashVideo={() => serverVideoReadyState = 0} />
            {/if}
        </div>
    </div>
    
	<label for="fname">
		<span>Output Name</span>
		<input id="fname" name="fname" type="text"/>
	</label>
    <label for="prompt">
		<span>Prompt</span>
		<input id="prompt" name="prompt" type="text" placeholder={promptPlaceholder} />
	</label>
	<label for="fps">
		<span>Output FPS</span>
		<input id="fps" name="fps" type="number" min="1" bind:value={fps} />
	</label>
	<label for="styles">
		<span>Style</span>
		<select id="styles" name="styles">
			{#each styles as ss}
				<option value={ss}>
					{ss}
				</option>
			{/each}
		</select>
	</label>
	<label for="type">
		<span>Type</span>
		<select id="type" name="type">
			{#each types as tp}
				<option value={tp}>
					{tp}
				</option>
			{/each}
		</select>
	</label>
	<label>
		<span>Sampling method</span>
		<select id="samplingMethod" name="samplingMethod">
			{#each samplingMethods as op}
				<option value={op}>
					{op}
				</option>
			{/each}
		</select>
	</label>

    <input type="submit" value={submitting ? "Processing..." : "Generate"} class="self-center cursor-pointer" disabled={submitting}>
    {#if errorText != null}
    <p class="text-red-400 text-center">An error occurred: {errorText}</p>
    {/if}
</form>

<style>
	label > span::after {
		content: ":"
	}
</style>