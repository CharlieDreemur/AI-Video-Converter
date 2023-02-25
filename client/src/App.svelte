<svelte:head>
	<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</svelte:head>
<script>
	import InputForm from "./util/InputForm.svelte";
    import Logo from "./Logo.svelte"

	let clientVideo = null;
	let serverVideoSrc = clientVideo == null ? null : `/dlv?dfn=${clientVideo.name}`;
	let fps = 1;

	// probably not the best way to do this
	let doLogoAnimation = false;
	let lastMoveTimeout = setTimeout(() => doLogoAnimation = true, 1000);
	function resetTimer() {
		doLogoAnimation = false;
		clearTimeout(lastMoveTimeout);
		lastMoveTimeout = setTimeout(() => doLogoAnimation = true, 1000);
	}
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<div on:mousemove={resetTimer}>

	<Logo anim={doLogoAnimation} />
	<h1 class="text-2xl text-center mt-4 mb-2">AI Video Convertor</h1>
	
	<InputForm bind:fps={fps} bind:videoData={clientVideo} bind:serverVideoSrc={serverVideoSrc} />
	
</div>
