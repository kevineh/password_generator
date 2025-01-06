
<template>
  <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
    <div class="relative py-3 sm:max-w-xl sm:mx-auto">
      <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
        <div class="max-w-md mx-auto">
          <div class="divide-y divide-gray-200">
            <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
              <h1 class="text-2xl font-bold text-gray-900 mb-8">Password Generator</h1>
              
              <PasswordDisplay 
                :password="generatedPassword"
                @copy="handleCopy"
              />

              <PasswordStrength 
                :password="generatedPassword"
              />

              <PasswordOptions 
                :options="passwordOptions"
                @update:options="updateOptions"
                @generate="generatePassword"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PasswordDisplay from './components/PasswordDisplay.vue'
import PasswordOptions from './components/PasswordOptions.vue'
import PasswordStrength from './components/PasswordStrength.vue'

export default {
  name: 'App',
  components: {
    PasswordDisplay,
    PasswordOptions,
    PasswordStrength
  },
  data() {
    return {
      generatedPassword: '',
      passwordOptions: {
        length: 12,
        useUppercase: true,
        useSymbols: true,
        useNumbers: true
      }
    }
  },
  methods: {
    updateOptions(newOptions) {
      this.passwordOptions = { ...newOptions }
    },
    async generatePassword() {
      try {
        const response = await fetch('http://localhost:8000/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.passwordOptions)
        })
        const data = await response.json()
        this.generatedPassword = data.password
      } catch (error) {
        console.error('Failed to generate password:', error)
      }
    },
    async handleCopy() {
      if (this.generatedPassword) {
        await navigator.clipboard.writeText(this.generatedPassword)
      }
    }
  }
}
</script>
