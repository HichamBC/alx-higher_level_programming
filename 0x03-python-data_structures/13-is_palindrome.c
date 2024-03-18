#include <stdlib.h>
#include "lists.h"

/**
 * linked_list_to_array - Converts a linked list to an array
 * @head: Pointer to the head of the linked list
 * @array: Pointer to store the resulting array
 *
 * Return: The number of elements in the resulting array
 */

int linked_list_to_array(listint_t *head, int **array)
{
	listint_t *p = head;
	int count = 0;
	int i;

	while (p != NULL)
	{
		count++;
		p = p->next;
	}

	*array = malloc(sizeof(int) * count);
	if (*array == NULL)
		return (0);

	p = head;
	for (i = 0; i < count; i++)
	{
		(*array)[i] = p->n;
		p = p->next;
	}

	return (count);
}


/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to a pointer to the head node of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int i;
	int j;
	int *arr = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);


	j = linked_list_to_array(*head, &arr) - 1;

	for (i = 0; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			is_palindrome = 0;
			break;
		}
	}

	free(arr);

	return (is_palindrome);
}
