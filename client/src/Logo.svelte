<script>
    export let anim = false;
</script>

<div class="flex justify-center">
    <img src="/favicon.png" width="100px" height="100px" class={`logo${anim ? " anim-pulse" : ""}`} />
</div>

<style>
    .logo {
        border-radius: 10px;
        margin: 10px;

        animation-iteration-count: 1;
    }
	.anim-pulse {
        box-shadow: 0 0 0 0 rgba(105, 167, 248, 1);
        transform: scale(1);

        animation: pulse 2s linear 1s infinite forwards;
	}
	@keyframes pulse {
        0% {
            /* transform: scale(0.99); */
            box-shadow: 0 0 0 0 rgba(105, 167, 248, 0.7);
        }
        
        70% {
            /* transform: scale(1); */
            box-shadow: 0 0 0 10px rgba(105, 167, 248, 0);
        }
        
        100% {
            /* transform: scale(0.99); */
            box-shadow: 0 0 0 0 rgba(105, 167, 248, 0);
        }
	}
</style>