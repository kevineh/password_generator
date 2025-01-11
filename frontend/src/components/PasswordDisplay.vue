<!--
  File: frontend/src/components/PasswordDisplay.vue
  Purpose: Main component for displaying generated password with show/hide and copy functionality
-->
<template>
  <div class="relative bg-gray-50 rounded-xl shadow-inner p-6 space-y-4">
    <div class="flex items-center space-x-4">
      <div class="flex-1 relative">
        <input
          :type="showPassword ? 'text' : 'password'"
          :value="password"
          readonly
          class="w-full px-6 py-4 text-xl bg-white border-2 border-blue-100 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300 font-mono"
        />
        <button
          @click="toggleVisibility"
          class="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-blue-500 transition-colors duration-200"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path v-if="showPassword" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z"/>
            <path v-else d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
          </svg>
        </button>
      </div>
      <button
        @click="copyToClipboard"
        class="px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 transform hover:scale-105 transition-all duration-200"
      >
        Copy
      </button>
    </div>
  </div>
</template>


<script>
export default {
  name: 'PasswordDisplay',
  props: {
    password: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      showPassword: false
    }
  },
  methods: {
    toggleVisibility() {
      this.showPassword = !this.showPassword
    },
    copyToClipboard() {
      this.$emit('copy')
    }
  }
}
</script>
