<!--
  File: frontend/src/components/PasswordOptions.vue
  Purpose: Component for password generation options (length, case, symbols, numbers)
-->
<template>
  <div class="space-y-6 bg-gray-50 rounded-xl shadow-inner p-6">
    <div class="space-y-4">
      <label class="block text-sm font-medium text-gray-700">Password Length: {{ options.length }}</label>
      <div class="flex items-center space-x-4">
        <span class="text-sm text-gray-500">10</span>
        <input
          type="range"
          v-model.number="localOptions.length"
          min="10"
          max="20"
          class="flex-1 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500"
        />
        <span class="text-sm text-gray-500">20</span>
      </div>
    </div>

    <div class="grid grid-cols-2 gap-4">
      <div class="relative flex items-start">
        <div class="flex items-center h-5">
          <input
            type="checkbox"
            v-model="localOptions.useUppercase"
            class="h-4 w-4 text-blue-500 border-gray-300 rounded focus:ring-blue-500"
          />
        </div>
        <div class="ml-3 text-sm">
          <label class="font-medium text-gray-700">Uppercase</label>
        </div>
      </div>

      <div class="relative flex items-start">
        <div class="flex items-center h-5">
          <input
            type="checkbox"
            v-model="localOptions.useSymbols"
            class="h-4 w-4 text-purple-500 border-gray-300 rounded focus:ring-purple-500"
          />
        </div>
        <div class="ml-3 text-sm">
          <label class="font-medium text-gray-700">Symbols</label>
        </div>
      </div>

      <div class="relative flex items-start">
        <div class="flex items-center h-5">
          <input
            type="checkbox"
            v-model="localOptions.useNumbers"
            class="h-4 w-4 text-cyan-500 border-gray-300 rounded focus:ring-cyan-500"
          />
        </div>
        <div class="ml-3 text-sm">
          <label class="font-medium text-gray-700">Numbers</label>
        </div>
      </div>
    </div>

    <button
      @click="generatePassword"
      class="w-full px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white text-lg font-semibold rounded-xl hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 transform hover:scale-105 transition-all duration-200"
    >
      Generate Password
    </button>
  </div>
</template>


<script>
export default {
  name: 'PasswordOptions',
  props: {
    options: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      localOptions: { ...this.options }
    }
  },
  watch: {
    localOptions: {
      handler(newValue) {
        this.$emit('update:options', newValue)
      },
      deep: true
    }
  },
  methods: {
    generatePassword() {
      this.$emit('generate')
    }
  }
}
</script>
