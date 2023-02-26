<svelte:head>
	<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</svelte:head>
<script>
	import VideoPlayer from "./util/VideoPlayer.svelte";
	import VideoUpload from "./util/VideoUpload.svelte";
	import InputForm from "./util/InputForm.svelte";
    import Logo from "./Logo.svelte";
    import { getFileExtension } from "./util/formSubmission";
    import DownloadButton from "./util/DownloadButton.svelte";

	let clientVideo = null;
	let serverVideoSrc = clientVideo == null ? null : `/dlv?dfn=${clientVideo.name}`;
	let fps = 1;
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<Logo />
<h1 class="text-2xl text-center mt-4 mb-2">AI Video Convertor</h1>

<InputForm bind:fps={fps} bind:videoData={clientVideo} bind:serverVideoSrc={serverVideoSrc} />