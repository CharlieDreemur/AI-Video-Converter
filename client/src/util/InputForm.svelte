<script>
    export let videoSrc = null; // bind
    export let videoName = null; // bind
    export let responseText = null; // bind

    const MAX_UPLOAD_SIZE_MB = 10;
    
    import App from "../App.svelte";
    import { getFileExtension, submitFormInBackground } from "./formSubmission.js";
    
	const uploadURL = "/api/diffuse";
	const samplingMethods = ["Euler a"]; // todo add
	const models = ["protogenX34OfficialR_1.ckpt"]; // todo add

	function clientVideoUpdated(e) {
		const file = e.target.files[0];
        const megaByteSize = file.size/Math.pow(10, 6);
        if (getFileExtension(file.name) !== "mp4") {
            errorText = `Files must be an mp4. (You uploaded a ${getFileExtension(file.name)})`;
            return;
        } else if (megaByteSize > MAX_UPLOAD_SIZE_MB) {
            errorText = `Max file size is ${MAX_UPLOAD_SIZE_MB} MB. (Your file is ${MAX_UPLOAD_SIZE_MB} MB.)`;
            return;
        }
		if (e == undefined) {
			videoSrc = null;
			videoName = null;
		} else {
			//el.srcObject = file
			videoSrc = window.URL.createObjectURL(file);
			videoName = file.name;
		}
        errorText = null;
	}

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

	const promptPlaceholder = "Make it spicy"; // todo generate random prompt
    let errorText = null;
    let submitting = false;
    $: console.log(errorText);
</script>

<form action={uploadURL} method="POST" enctype="multipart/form-data" class="p-10 max-w-lg mx-auto bg-white rounded-xl shadow-lg space-y-4 grid" on:submit={submitVideoForm}>
	<label for="video">
		<span>Input video</span>
		<input id="video" name="video" type="file" accept="video/mp4" on:change={clientVideoUpdated} required />
	</label>
	<!--<span>{promptHint}</span>-->
	<label for="prompt">
		<span>Prompt</span>
		<input id="prompt" name="prompt" type="text" placeholder={promptPlaceholder} />
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

    <input type="submit" value={submitting ? "Processing..." : "Upload"} class="self-center cursor-pointer" disabled={submitting}>
    {#if errorText != null}
    <p class="text-red-400">An error occurred: {errorText}</p>
    {/if}
</form>

<style>
	label > span::after {
		content: ":"
	}
</style>