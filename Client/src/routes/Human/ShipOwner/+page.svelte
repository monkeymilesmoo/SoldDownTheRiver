<style>
	@import '/static/FormPages.css';
</style>
<script>
	import moment from 'moment';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { handleSave } from '../handleSave.js';
	import { handleDelete } from '../handleDelete.js';
	import { handleGetHuman } from '../handleGetHuman.js';
	import { handleGetRoles } from '../handleGetRoles.js';
	// import { handleGetAKA } from '../handleGetAKA.js';
	// import { handleSaveAkaName } from '../handleSaveAkaName.js';
	// import { handleDeleteAkaName } from '../handleDeleteAkaName.js';
	import {Session} from "../../Session.js";


	let FormValid=true
	let isLoading = true;
	let HumanId="";

	let Human=[];
	let Roles=[];
	// let AkaNames = [];

	async function setHuman(data) {
		Human=data;
	}
	
	async function setRoles(data) {
		Roles = data;
	}
	async function setAkaNames(data) {
		AkaNames = data;
	}
	onMount(async () => {
		await Session.handleSession();
		const urlParams = new URLSearchParams(window.location.search);
		HumanId = urlParams.get("HumanId") || "";
		
		await Promise.all([
			// handleGetAKA(Session.SessionId,HumanId, setAkaNames),
			handleGetHuman(Session.SessionId,HumanId, setHuman),
			handleGetRoles(Session.SessionId,setRoles)
		]);
	 
		isLoading = false;
	});
</script>


{#if isLoading}
	<div class="loading-screen">
		<div class="spinner"></div>
	</div>
{:else}
<div class="section">
	<a href="/Role?RoleId=ShipOwner">Back to Ship Owners</a>
	<div class="ActionBox">
		<h3 class="title is-2">Edit Human</h3>
	<form>
		<div class="field">
			<label class="label" for="FirstName">First Name:</label>
			<div class="control">
				<input class="input" type="text" id="FirstName" bind:value={Human.FirstName} required>
			</div>
		</div>
		<div class="field">
			<label class="label" for="MiddleName">Middle Name:</label>
			<div class="control">
				<input class="input" type="text" id="MiddleName" bind:value={Human.MiddleName}>
			</div>
		</div>
		<div class="field">
			<label class="label" for="LastName">Last Name:</label>
			<div class="control">
				<input class="input" type="text" id="LastName" bind:value={Human.LastName} required>
			</div>
		</div>
		<div class="field">
			<label class="label" for="Role">Role:</label>
			<div class="control">
				<select id="RoleId" bind:value={Human.RoleId}>
					<option value="">Select Role</option>
					{#each Roles as Role}
						<option value={Role.RoleId}>{Role.Role}</option>
					{/each}
				</select>
			</div>
		</div>
		
		<div class="field">
			<label class="label" for="Notes">Notes:</label>
			<div class="control">
				<textarea class="textarea" id="Notes" bind:value={Human.Notes}></textarea>
			</div>
		</div>
		

		
		<div class="field">
			<div class="control">
				<button class="button is-primary" type="button" on:click={() => handleSave(Session.SessionId,Human.HumanId, Human.FirstName, Human.MiddleName, Human.LastName, Human.Notes, Human.RoleId, FormValid)}>Save</button>
				<!-- {#if Human.HumanId.length}
					<button class="button is-danger" type="button" on:click={() => handleDelete(Session.SessionId,Human.HumanId)}>Delete</button>
				{/if} -->
			</div>
		</div>
	</form>
	{#if Human.LastModified}
		<small>Last Modified: {moment.utc(Human.LastModified).local().fromNow()}</small>
	{/if}
</div>
</div>
	{/if}
