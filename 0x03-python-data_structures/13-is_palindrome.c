#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *p1 = *head;
	listint_t *p2 = *head;
	listint_t *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (p2 != NULL && p2->next != NULL)
	{
		p2 = p2->next->next;

		temp = p1->next;
		p1->next = prev;
		prev = p1;
		p1 = temp;
	}

	if (p2 != NULL)
		p1 = p1->next;

	while (prev != NULL && p1 != NULL)
	{
		if (prev->n != p1->n)
			return (0);
		prev = prev->next;
		p1 = p1->next;
	}

	return (1);
}
