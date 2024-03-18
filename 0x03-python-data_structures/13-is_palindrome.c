#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

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
	int count = 0;
	int is_palindrome = 1;
	listint_t *ptr = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}

	arr = malloc(sizeof(int) * count);
	if (arr == NULL)
	{
		return (0);
	}

	ptr = *head;
	for (i = 0; i < count; i++)
	{
		arr[i] = ptr->n;
		ptr = ptr->next;
	}

	for (i = 0, j = count - 1; i < j; i++, j--)
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
