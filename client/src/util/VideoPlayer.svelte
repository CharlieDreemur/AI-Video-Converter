<script>
	export let srcURL;
	// export let clientVideoWidth;
	// export let clientVideoHeight;
    // width={clientVideoHeight} height={clientVideoWidth}
    // bind:clientWidth={clientVideoWidth} bind:clientHeight={clientVideoHeight}
</script>

<div>
    {#if srcURL != null && srcURL != ""}
    <!-- svelte-ignore a11y-media-has-caption -->
    <video controls>
        <source src={srcURL} type="video/{srcURL.slice(-srcURL.lastIndexOf('.'))}">
        Can't preview: Your browser doesn't support the video tag.
    </video>
    <i class="fa fa-trash"></i>
    {/if}
</div>
