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

	let randomLeafData: any = $state({
		'jp maple 2': { f: [], b: [] },
		'bonfire sugar maple 2': { f: [], b: [] },
		'tulip tree 2': { f: [], b: [] },
		'american elm 2': { f: [], b: [] }
	})

	const types = ['red maple', 'jp maple', 'american elm', 'quaking aspen', 'tulip tree']
	const randomTypes = ['jp maple 2', 'bonfire sugar maple 2', 'tulip tree 2', 'american elm 2']
	let selectedType = $state(randomTypes[0])
	let isRandom = $derived(randomTypes.includes(selectedType))

	let selectedTypeData: any = $derived(
		isRandom ? randomLeafData[selectedType] : leafData[selectedType]
	)

	onMount(async () => {
		const responses = await Promise.all([fetch('/random.json'), fetch('/data.json')])
		const [randomData, data] = await Promise.all(responses.map((res) => res.json()))

		randomLeafData = randomData
		leafData = data
	})
</script>

<div class="md:grid grid-cols-3 md:h-full">
	<div class="h-full m-2">
		<div class="italic">Color of Multiple Leaves on One Tree <br /> At One Point in Time</div>
		{#each randomTypes as type}
			<div class="m-2">
				<a
					class="hover:font-bold"
					style={`${type === selectedType ? 'font-weight: bold' : ''}`}
					href="#"
					onclick={() => {
						selectedType = type
					}}>&bull; {type}</a
				>
			</div>
		{/each}
		<div class="italic">Color of One Leaf Over Time (WIP)</div>
		{#each types as type}
			<div class="m-2">
				<a
					class="hover:font-bold"
					style={`${type === selectedType ? 'font-weight: bold' : ''}`}
					href="#"
					onclick={() => {
						selectedType = type
					}}>&bull; {type}</a
				>
			</div>
		{/each}
	</div>
	<div class="col-span-2 grid grid-rows-2 h-full">
		<!-- front face colors -->
		{#each ['f', 'b'] as face}
			<div class="h-full">
				<h2 class="font-bold text-lg">{face == 'f' ? 'Front' : 'Back'} of Leaf Colors</h2>
				<div class="grid grid-cols-3 md:grid-cols-6 *:aspect-square">
					{#each selectedTypeData[face] as datum}
						<div
							class="group relative"
							style={`background-color: ${lab_hexrgb([datum['l'], datum['a'], datum['b']])}`}
						>
							<div class="group-hover:block hidden absolute p-2 bg-inherit z-50">
								<div>{datum['date']}</div>
								<div>L: {Math.round(datum['l'] * 1000) / 1000}</div>
								<div>A: {Math.round(datum['a'] * 1000) / 1000}</div>
								<div>B: {Math.round(datum['b'] * 1000) / 1000}</div>
								<div>
									sRGB Hex: {lab_hexrgb([datum['l'], datum['a'], datum['b']])}
								</div>
							</div>
						</div>
					{/each}
				</div>
			</div>
		{/each}
	</div>
	<footer class="m-2">
		By Shengdong Li<br /> andy.shengdong.li@gmail.com<br />
		<a
			class="text-blue-600 visited:text-purple-600"
			href="https://github.com/SpicyRicecaker/color-converter">source</a
		>
	</footer>
</div>
