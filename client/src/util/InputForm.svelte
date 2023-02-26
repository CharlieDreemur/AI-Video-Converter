<script>
    export let videoSrc = null; // bind
    export let responseText = null; // bind
    
    import { submitFormInBackground } from "./formSubmission.js";
    
	const uploadURL = "/upv";
	const samplingMethods = ["Euler a", "idk"]; // todo add
	const models = ["protogenX34OfficialR_1.ckpt"]; // todo add
    let videoName = null;

	function clientVideoUpdated(e) {
		const file = e.target.files[0];
		console.log(file);
		if (e == undefined) {
			videoSrc = null;
			videoName = null;
		} else {
			//el.srcObject = file
			videoSrc = window.URL.createObjectURL(file);
			videoName = file.name;
		}
	}

    function submitVideoForm(e) {
        submitFormInBackground(e)
            .then(res => {
                // send up
                responseText = res.text();
            })
            .catch(err => errorText = err);
    }

    // let clientPrompt = null; //#prompt bind:value={clientPrompt}
	//$: promptHint = clientPrompt.length < 8 ? "Add more details" : null;

	const promptPlaceholder = "Make it spicy"; // todo generate random prompt
    let errorText = null;
</script>

<form action={uploadURL} method="POST" enctype="multipart/form-data" class="p-10 max-w-lg mx-auto bg-white rounded-xl shadow-lg space-y-4 grid" on:submit={submitVideoForm}>
	<label for="video">
		<span>Input video</span>
		<input id="video" name="video" type="file" accept="video/*" on:change={clientVideoUpdated} required />
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

    <input type="submit" value="Upload" class="self-center cursor-pointer">
    {#if errorText != null}
    <p class="text-red">An error occurred: {errorText}</p>
    {/if}
</form>

<style>
	label > span::after {
		content: ":"
	}
</style>