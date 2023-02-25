<script>
	// import('https://cdn.tailwindcss.com');

	import VideoPlayer from "src/util/VideoPlayer.svelte";

	let uploadURL = "/api/diffuse"; // todo
	
	let clientVideoSrc = null;
	let serverVideoSrc = null;
	
	function clientVideoUpdated(e) {
		const file = e.target.files[0];
		clientVideoSrc = URL.createObjectURL(file);
		clientVideoName = URL.createObjectURL(file.name);
	}

	function getPromptHint() {
		// todo look at clientPrompt
		return "hi";
	}

	// $:
	let promptHint = getPromptHint();
	let clientPrompt = null;
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h1>AIVideoConvertor</h1>
<Test />
<p>
	Select a file to upload.
</p>

<form action={uploadURL} method="POST" enctype="multipart/form-data">
    <input id="video" name="video" type="file" accept="video/*" on:change={clientVideoUpdated} required>
	<p>{promptHint}</p>
    <input id="prompt" name="prompt" type="text" bind:value={clientPrompt} required>
    <input type="submit" class="button" value="Upload">
</form>

<div class="grid-cols-2">
	<div>
		<p>Input</p>
		<p>{promptHint}</p>
		<VideoPlayer srcURL={clientVideoSrc} />
	</div>
	<div>
		<p>Output</p>
		<VideoPlayer srcURL={serverVideoSrc} />
	</div>
</div>