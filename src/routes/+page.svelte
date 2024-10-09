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
			<div>
				<a
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
						style={`background-color: ${lab_hexrgb([datum['l'], datum['a'], datum['b']])}`}
					></div>
				{/each}
			</div>
		</div>

		<!-- bace face colors -->
		<div class="h-full">
			<div class="grid grid-cols-8 *:aspect-square overflow-auto">
				{#each selectedTypeData['b'] as datum}
					<div
						style={`background-color: ${lab_hexrgb([datum['l'], datum['a'], datum['b']])}`}
					></div>
				{/each}
			</div>
		</div>
	</div>
</div>
