<!--
  File: frontend/src/components/PasswordDisplay.vue
  Purpose: Main component for displaying generated password with show/hide and copy functionality
-->
<template>
  <div class="relative">
    <div class="flex items-center space-x-2">
      <div class="flex-1 relative">
        <input
          :type="showPassword ? 'text' : 'password'"
          :value="password"
          readonly
          class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          @click="toggleVisibility"
          class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path v-if="showPassword" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z"/>
            <path v-else d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
          </svg>
        </button>
      </div>
      <button
        @click="copyToClipboard"
        class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
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
