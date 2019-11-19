<template>
  <div class="recommend">
    <user-recommend></user-recommend>
  </div>
</template>

<script>
    import ImageStream from './ImagePage/ImageStream'
    export default {
        name: "Recommend",
        components: {
            'user-recommend': ImageStream
        }
    }
</script>

<style scoped>

</style>
