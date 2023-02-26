<svelte:head>
	<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</svelte:head>
<script>
	import VideoPlayer from "./util/VideoPlayer.svelte";
	import InputForm from "./util/InputForm.svelte";
    import Logo from "./Logo.svelte";
    import { getFileExtension } from "./util/formSubmission";
    import DownloadButton from "./util/DownloadButton.svelte";

	let clientVideoSrc = null;
	let clientVideoName = null;
	let serverVideoSrc = `/dlv?dfn=${clientVideoName}`;
	let serverVideoReadyState = 0; // 0 = not started, 1 = processing, 2 = ready

	let serverResponse = null;
	$: {
		if (serverResponse != null) {
			// todo should be 1 until ready
			serverVideoReadyState = 2;
		}
	}
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<Logo />
<h1 class="text-2xl text-center mt-4 mb-2">AI Video Convertor</h1>

<InputForm bind:videoSrc={clientVideoSrc} bind:responseText={serverResponse} bind:videoName={clientVideoName} />

<div class="grid sm:grid-cols-2 justify-center text-center mt-8">
	<div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500">
		<p>Input</p>
		<VideoPlayer bind:srcURL={clientVideoSrc} type={getFileExtension(clientVideoName)} />
	</div>
	<div class="m-2 p-2 border-solid border-2 ring-offset-2 border-gray-500">
		<p>Output</p>
		{#if serverVideoSrc === 2}
			<DownloadButton bind:url={serverVideoSrc} />
			<VideoPlayer bind:srcURL={serverVideoSrc} type={"mp4"} />
		{/if}
	</div>
</div>