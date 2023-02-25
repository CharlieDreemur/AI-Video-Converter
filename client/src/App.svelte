<script>
	import VideoPlayer from "./util/VideoPlayer.svelte";

	let uploadURL = "/api/diffuse";
	
	const samplingMethods = ["Euler a", "idk"]; // todo add
	const models = ["protogenX34OfficialR_1.ckpt"]; // todo add
	
	let clientVideoSrc = null;
	let serverVideoSrc = null;
	
	function clientVideoUpdated(e) {
		const file = e.target.files[0];
		console.log(file);
		if (e == undefined) {
			clientVideoSrc = null;
			clientVideoName = null;
		} else {
			//el.srcObject = file
			clientVideoSrc = window.URL.createObjectURL(file);
			clientVideoName = window.URL.createObjectURL(file.name);
		}
	}

	let clientPrompt = null;
	
	//$: promptHint = clientPrompt.length < 8 ? "Add more details" : null;

	const promptPlaceholder = "Make it spicy"; // todo generate random prompt
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h1>AI Video Convertor</h1>

<form action={uploadURL} method="POST" enctype="multipart/form-data">
	<label for="video">
		<span>Input video</span>
		<input id="video" name="video" type="file" accept="video/*" on:change={clientVideoUpdated} required />
	</label>
	<!--<span>{promptHint}</span>-->
	<label for="prompt">
		<span>Prompt</span>
		<input id="prompt" name="prompt" type="text" bind:value={clientPrompt} placeholder={promptPlaceholder} />
	</label>
	<label for="model">
		<span>Model</span>
		<select>
			{#each models as op}
				<option value={op}>
					{op}
				</option>
			{/each}
		</select>
	</label>
	<label>
		<span>Sampling method</span>
		<select>
			{#each samplingMethods as op}
				<option value={op}>
					{op}
				</option>
			{/each}
		</select>
	</label>

    <input type="submit" value="Upload">
</form>

<div class="grid-cols-2">
	<div>
		<p>Input</p>
		<VideoPlayer srcURL={clientVideoSrc} />
	</div>
	<div>
		<p>Output</p>
		<VideoPlayer srcURL={serverVideoSrc} />
	</div>
</div>