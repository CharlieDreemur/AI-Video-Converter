<script>
	// import('https://cdn.tailwindcss.com');

	import VideoPlayer from "./util/VideoPlayer.svelte";

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
		if (clientPrompt == null || clientPrompt === "") {
			return "Try adding some text.";
		}
		return null;
	}
	let clientPrompt = null;
	
	// $:
	$: promptHint = clientPrompt == null ? "null" : "not null";//getPromptHint();
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h1>AIVideoConvertor</h1>
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
		<VideoPlayer srcURL={clientVideoSrc} />
	</div>
	<div>
		<p>Output</p>
		<VideoPlayer srcURL={serverVideoSrc} />
	</div>
</div>