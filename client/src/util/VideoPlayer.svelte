<script>
	export let srcURL; // bind
	export let type = "mp4";
    export let trashVideo;

	// export let clientVideoWidth;
	// export let clientVideoHeight;
    // width={clientVideoHeight} height={clientVideoWidth}
    // bind:clientWidth={clientVideoWidth} bind:clientHeight={clientVideoHeight}
</script>

<div>
    {#if srcURL != null && srcURL != ""}
    <!-- svelte-ignore a11y-media-has-caption -->
    <video controls>
        <source src={srcURL} type="video/{type}">
        Can't preview: Your browser doesn't support the video tag.
    </video>
    <i class="fa fa-trash cursor-pointer" on:click|stopPropagation={trashVideo}></i>
    {/if}
</div>
