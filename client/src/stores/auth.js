import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { getUser } from '@/services/auth'


export const useAuthStore = defineStore('auth', () => {
    const user = ref(null);

    const isLoggedIn = computed(() => {
        return user.value !== null
    })

    const authenticate = async () => {
        // make a call to backend -> /users -> this returns user's object. 
        // if this returns an error, redirect the user to the login page -> '/login'
        // if user is returned, initialise this.user with objects.
        user.value = await getUser()

    }

    return { user, isLoggedIn, authenticate }

})
