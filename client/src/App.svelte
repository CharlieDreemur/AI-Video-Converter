<svelte:head>
	<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</svelte:head>
<script>
	import VideoPlayer from "./util/VideoPlayer.svelte";
	import InputForm from "./util/InputForm.svelte";

	let clientVideoSrc = null;
	let clientVideoName = null;
	let serverVideoSrc = null; // todo get from form response

	let serverResponse = null;
	// todo handle changes to serverResponse
	// parse JSON and update serverVideoSrc
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h1 class="text-2xl text-center mt-6 mb-2">AI Video Convertor</h1>

<InputForm bind:videoSrc={clientVideoSrc} bind:responseText={serverResponse} bind:videoName={clientVideoName} />

<div class="grid sm:grid-cols-2 justify-center text-center mt-8">
	<div>
		<p>Input</p>
		<VideoPlayer bind:srcURL={clientVideoSrc} type={clientVideoName != null ? clientVideoName.substring(clientVideoName.lastIndexOf(".") + 1) : null} />
	</div>
	<div>
		<p>Output</p>
		<VideoPlayer bind:srcURL={serverVideoSrc} type={"mp4"} />
	</div>
</div>