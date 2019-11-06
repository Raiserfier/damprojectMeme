<template>
  <div class="title">
<!--  Title-->
<!--  Image Stream-->
    <image-stream></image-stream>
  </div>
</template>

<script>
    import ImageStream from "./ImagePage/ImageStream";
    export default {
        name: "Title",
        components: { 'image-stream': ImageStream }
    }
</script>

<style scoped>

</style>
