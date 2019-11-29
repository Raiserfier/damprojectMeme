<template>
  <div class="title">
<!--  Title-->
<!--  Image Stream-->
    <h2 class="Titleeeee">{{this.$route.params.key}}</h2>
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
.Titleeeee {
    padding-top: 90px;
    padding-left: 16%;
    /*cursor: pointer;*/
    text-decoration: none;
    font-family: HYZhengYuan-75W, sans-serif;
    font-size: 35px;
    font-weight: 300;
    margin: 0;
    z-index: 100;
}
</style>
