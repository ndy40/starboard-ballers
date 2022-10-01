<template>
  <div class="container mx-auto w-2/4">
    <p>Big sky</p>
    <p class="bg-sky-500 hover:bg-sky-700"> {{ authStore.isLoggedIn ? 'Yes' : 'No'}}</p>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

onMounted(() => {
  authStore.authenticate().then((value) => console.log(value))
})

</script>
<style scoped>

</style>
