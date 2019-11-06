<template>
  <div id="app">
    <Nav></Nav>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>
import Nav from './components/Nav'
export default {
  name: 'App',
  components: { 'Nav': Nav }
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
