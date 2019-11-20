<template>
  <div id="app">
    <Nav></Nav>
    <transition name="fade" mode="out-in">
      <router-view :key="key"/>
    </transition>
  </div>
</template>

<script>
import Nav from './components/Nav'
export default {
  name: 'App',
  components: { 'Nav': Nav },
  data() {
      return {
          key: 0
      }
  },
  watch:{
     '$route': function () {
         // console.log("route change");
         this.key += 1;
     }
  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .15s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
.fade-leave {
  opacity: 1;
}
</style>
