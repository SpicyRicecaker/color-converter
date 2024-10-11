<script lang="ts">
	import '../app.css'
	import { lab_hexrgb } from '$lib/index'

	import { onMount } from 'svelte'

	let leafData: any = $state({
		'red maple': { f: [], b: [] },
		'jp maple': { f: [], b: [] },
		'american elm': { f: [], b: [] },
		'quaking aspen': { f: [], b: [] },
		'tulip tree': { f: [], b: [] }
	})

	const types = ['red maple', 'jp maple', 'american elm', 'quaking aspen', 'tulip tree']
	let selectedType = $state(types[0])

	let selectedTypeData: any = $derived(leafData[selectedType])

	onMount(async () => {
		const response = await fetch('/data.json')
		leafData = await response.json()
	})
</script>

<div class="grid grid-cols-3 h-full">
	<div class="h-full">
		{#each types as type}
			<div class="m-2">
				<a
					class="hover:font-bold"
					href="#"
					onclick={() => {
						selectedType = type
					}}>{type}</a
				>
			</div>
		{/each}
	</div>
	<div class="col-span-2 grid grid-rows-2 h-full">
		<!-- front face colors -->
		<div class="h-full">
			<div class="grid grid-cols-8 *:aspect-square overflow-auto">
				{#each selectedTypeData['f'] as datum}
					<div
						class="group p-2"
						style={`background-color: ${lab_hexrgb([datum['l'], datum['a'], datum['b']])}`}
					>
						<div class="group-hover:block hidden">{datum['date']}</div>
						<div class="group-hover:block hidden">L: {Math.round(datum['l'] * 1000) / 1000}</div>
						<div class="group-hover:block hidden">A: {Math.round(datum['a'] * 1000) / 1000}</div>
						<div class="group-hover:block hidden">B: {Math.round(datum['b'] * 1000) / 1000}</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- bace face colors -->
		<div class="h-full">
			<div class="grid grid-cols-8 *:aspect-square overflow-auto">
				{#each selectedTypeData['b'] as datum}
					<div
						class="group p-2"
						style={`background-color: ${lab_hexrgb([datum['l'], datum['a'], datum['b']])}`}
					>
						<div class="group-hover:block hidden">{datum['date']}</div>
						<div class="group-hover:block hidden">L: {Math.round(datum['l'] * 1000) / 1000}</div>
						<div class="group-hover:block hidden">A: {Math.round(datum['a'] * 1000) / 1000}</div>
						<div class="group-hover:block hidden">B: {Math.round(datum['b'] * 1000) / 1000}</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>
