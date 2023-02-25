<script>
    export let videoSrc = null; // bind
    export let videoName = null; // bind
    export let responseText = null; // bind
    export let fps = 1; // bind
    export let videoData = null;
    export let serverVideoSrc = null;
    
    import { getRandomAdjective } from "./randomAdjective.js";
    import { submitFormInBackground } from "./formSubmission.js";
    import VideoUpload from "./VideoUpload.svelte";
    
	const uploadURL = "/api/diffuse";
	const samplingMethods = ["Euler a"]; // todo add
	const models = ["protogenX34OfficialR_1.ckpt"]; // todo add

    function submitVideoForm(e) {
        submitting = true;
        submitFormInBackground(e)
            .then(res => {
                submitting = false;
                // send up
                responseText = res.text();
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
	let serverResponse = null;
	$: {
		if (serverResponse != null) {
			// todo should be 1 until ready
			serverVideoReadyState = 2;
		}
	}
</script>

<form action={uploadURL} method="POST" enctype="multipart/form-data" class="p-10 max-w-xl mx-auto bg-white rounded-xl shadow-lg space-y-4 grid" on:submit|preventDefault={submitVideoForm}>
	<div class="grid sm:grid-cols-2 justify-center text-center mt-8">
        <VideoUpload bind:file={videoData} />
        <div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500">
            <p>Output</p>
            {#if serverVideoSrc === 2}
                <DownloadButton bind:url={serverVideoSrc} />
                <VideoPlayer bind:srcURL={serverVideoSrc} type={"mp4"} />
            {/if}
        </div>
    </div>
    
    <label for="prompt">
		<span>Prompt</span>
		<input id="prompt" name="prompt" type="text" placeholder={promptPlaceholder} />
	</label>
	<label for="fps">
		<span>Output FPS</span>
		<input id="fps" name="fps" type="number" min="1" bind:value={fps} />
	</label>
	<label for="model">
		<span>Model</span>
		<select id="model" name="model">
			{#each models as op}
				<option value={op}>
					{op}
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
    <p class="text-red-400">An error occurred: {errorText}</p>
    {/if}
</form>

<style>
	label > span::after {
		content: ":"
	}
</style>