<template>
	<Provider>
		<component
			:is="layoutComponent"
			:class="[`theme-${themeName}`, `layout-${layoutComponentName}`, themeName, { 'opacity-0': loading }]"
		>
			<RouterView v-slot="{ Component: RouterComponent }">
				<transition :name="`router-${routerTransition}`" mode="out-in" appear>
					<component
						:is="RouterComponent"
						:key="(route?.name?.toString() || '') + forceRefresh"
						:class="[`theme-${themeName}`, `layout-${layoutComponentName}`, themeName]"
					/>
				</transition>
			</RouterView>
		</component>

		<SplashScreen :show="loading" />
		<SearchDialog v-if="isLogged" />
	</Provider>
</template>

<script lang="ts" setup>
import type { Layout, RouterTransition, ThemeNameEnum } from "@/types/theme.d"
import Blank from "@/app-layouts/Blank/index.vue"
import Provider from "@/app-layouts/common/Provider.vue"
import SplashScreen from "@/app-layouts/common/SplashScreen.vue"
import HorizontalNav from "@/app-layouts/HorizontalNav/index.vue"
import SearchDialog from "@/components/common/SearchDialog.vue"
import { useAuthStore } from "@/stores/auth"
import { useMainStore } from "@/stores/main"
import { useThemeStore } from "@/stores/theme"
import { type Component, computed, onBeforeMount, ref, watch } from "vue"
import { type RouteLocationNormalized, useRoute, useRouter } from "vue-router"
import "@/assets/scss/index.scss"

const router = useRouter()
const route = useRoute()
const loading = ref(true)

const layoutComponents = {
	HorizontalNav,
	Blank
}

const themeStore = useThemeStore()
const mainStore = useMainStore()
const authStore = useAuthStore()

const forceRefresh = computed<number>(() => mainStore.forceRefresh)
const forceLayout = ref<Layout | null>(null)
const layout = computed<Layout>(() => themeStore.layout)
const layoutComponentName = computed<Layout>(() => forceLayout.value || layout.value)
const layoutComponent = computed<Component>(() => layoutComponents[layoutComponentName.value])
const routerTransition = computed<RouterTransition>(() => themeStore.routerTransition)
const themeName = computed<ThemeNameEnum>(() => themeStore.themeName)
const isLogged = computed(() => authStore.isLogged)

function checkForcedLayout(route: RouteLocationNormalized) {
	if (route.meta?.forceLayout) {
		forceLayout.value = route.meta.forceLayout
	} else {
		forceLayout.value = null
	}
}

watch(layoutComponentName, () => {
	loading.value = false
})

router.afterEach(route => {
	checkForcedLayout(route)
})

onBeforeMount(() => {
	checkForcedLayout(useRoute())

	setTimeout(() => {
		loading.value = false
	}, 500)
})
</script>
